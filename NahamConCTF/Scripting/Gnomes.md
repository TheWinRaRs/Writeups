# Gnomes

This was a fairly simple scripting challenge. This relies on getting enough gold for each weapon tier, and working your way up.

```py
from pwn import *
import re

r = remote('jh2i.com', 50031)
weapons = [100000, 10000, 2000, 1000, 100]
while True:
    prompt = r.recvuntil('>').decode()
    print(prompt)
    gold = int(re.findall('Gold: \d+', prompt)[0].split()[1])
    print(gold)
    try: # The try and except was because I'm dumb and when you have nothing in the weapons list you get an index error
        if gold >= weapons[-1]:
            weapons.pop()
            r.sendline('6')
            r.recvuntil(':')
            r.sendline(str(5 - len(weapons)))
        else:
            r.sendline(str(len(weapons) + 1))
    except:
        r.sendline('1')
```
Flag:
#### flag{it_was_in_fact_you_that_was_really_powerful}
