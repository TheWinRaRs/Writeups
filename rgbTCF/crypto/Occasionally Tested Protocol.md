# Occasionally Tested Protocol

Looking at the code, we can see it uses `random.randint` to generate the one time pad.

The thing that is most of note is that it seeds python's random generator using the current time.

Not only this, it prints out the first 10 random numbers outputted by the generator by doing `random.randint(5, 10000)` and printing the output 10 times.

We can record the time shortly after we connect to the server.

Chances are, we won't have the exact right value.

However, we can use the 10 random numbers as a form of "check" - essentially, we can bruteforce the time based seed within a sensible range, test the seed against the 10 random numbers we know come from the generator, and find the correct one.

Once we find the correct one, it's trivial to generate the byte array and XOR back to get the flag.

script below:
```python
import os
os.environ['TERM'] = 'linux'
os.environ['TERMINFO'] = '/etc/terminfo'
from pwn import *
from random import seed, randint as w
from time import time
def getnums(secs):
    seed(secs)
    ans = []
    for _ in range(10):
        ans.append(w(5, 10000))
    return ans
p = remote('167.172.123.213', 12345)
recorded = int(time())
p.recvline()
nums = [int(x) for x in p.recvlines(10)]
p.recvuntil(b"Here's another number I found: ")
enc = int(p.recvline())
knownseed = None
for possible in range(recorded-100,recorded+100):
    nums2 = getnums(possible)
    if nums == nums2:
        knownseed = possible
        break
seed(knownseed)
for _ in range(10):
    print(w(5, 10000))
b = bytearray([w(0, 255) for _ in range(40)])
enc = enc.to_bytes(255,'little')
print(enc)
flag = bytearray([l ^ p for l, p in zip(enc, b)])
print(flag)
```


#### Flag: rgbCTF{random_is_not_secure}
