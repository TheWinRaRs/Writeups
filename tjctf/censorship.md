# Censorship

```python
from pwn import *
r = remote("p1.tjctf.org", 8003)
out = (r.recvline())
print(out)
out = eval(out.split('is ')[2][:-2])
r.sendline(str(out))
print(r.recvline())
print(r.recvline())
This works and I don't know why
tjctf{TH3_1llum1n4ti_I5_R3aL}
```

