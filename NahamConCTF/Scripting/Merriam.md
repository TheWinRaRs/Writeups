# Merriam

```python
from pwn import *
import enchant

wordlist = enchant.Dict('en-US')

notin = lambda x: not wordlist.check(x)
isin = lambda x: wordlist.check(x)

r = remote('jh2i.com', 50012)
while True:
    line = r.recvline().decode()
    print(line)
    words = r.recvline().decode()
    print(words)
    words = words.split()
    func = notin if 'NOT' in line else isin
    if 'CHRONOLOGICAL' in line:
        result = ' '.join(word for word in words if func(word))
    elif 'ALPHABETICAL' in line:
        result = ' '.join(sorted(word for word in words if func(word)))
    else:
        result = str(sum(map(func, words)))
    r.sendline(result)
    print(r.recvline().decode())
```
####  flag{you_know_the_dictionary_so_you_are_hired}
