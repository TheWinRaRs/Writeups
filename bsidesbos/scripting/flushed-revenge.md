# Flushed Revenge

Run script then profit
```python
from pwn import *
import string

def recvline(r):
    lines = [r.recvline().decode()[1:] for _ in range(8)]
    chunks = [[l[i:i+6] for i in range(0, len(l), 7)] for l in lines]
    chars = list(zip(*chunks))
    return chars

def recvall(r, timeout=1):
    while i := r.recvline(timeout=timeout).decode():
        pass

mapping = {}

with remote('challenge.ctf.games', 30877) as r:
    recvall(r, timeout=5)
    for c in string.ascii_letters + string.digits + '+=/':
        r.sendline(c)
        r.recvline()
        result = recvline(r)[0]
        mapping[result] = c
        print(c, '\n'.join(result), sep='\n')
        recvall(r)
    r.sendline('base64 flag.png')
    r.recvline()
    with open('b64flag.hd', 'w') as f:
        while True:
            for i in recvline(r):
                print('\n'.join(i))
                result = mapping.get(i, ' ')
                f.write(result)
```

