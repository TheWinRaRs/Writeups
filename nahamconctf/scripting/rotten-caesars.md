# rotten: caesars

```python
from pwn import *
from string import ascii_letters

def shift(string, offset):
    result = ''
    for c in string:
        result += chr((ord(c)+offset-97)%26 + 97) if c in ascii_letters else c
    return result

flag = [' ']*50

r = remote('jh2i.com', 50034)
r.sendline(r.recvline())
while True:
    line = r.recvline().decode()
    offset = ord('s') - ord(line[0])
    decrypted = shift(line, offset)
    if 'character' in decrypted:
        flag[int(decrypted.split()[6])] = decrypted[-3]
    r.sendline(decrypted)
    print(*flag, sep='')
```

## flag{now\_you\_know\_your\_caesars}

