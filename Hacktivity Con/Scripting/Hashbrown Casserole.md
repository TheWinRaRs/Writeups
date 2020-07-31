# Hashbrown Casserole

When we connect, we are given a hashsum (sha1/md5) and asked to send data, that when hashed, begins with a particular few bytes.

We have to bruteforce a value to create this, 50 times


```python

from pwn import *
from pwnlib.util.iters import mbruteforce

from hashlib import md5, sha1
methods = {"md5sum":md5, "sha1sum":sha1}
host = ("jh2i.com", 50005)
r = remote(*host)
for x in range(50):
    r.recvuntil('Enter the data required for the first part of the ')

    method = r.recvuntil(' ')[:-1]
    sum = methods[method]
    r.recvuntil(': ')
    hash = r.recvline().strip()
    import string
    #chars = string.printable
    chars = [chr(c) for c in range(256)]
    chars.remove('\r')
    chars.remove('\n')
    def checkhash(string):
        if sum(string).hexdigest().startswith(hash):
            return True
        return False

    print("Goal: " + hash)
    print("Method: " + method)
    key = mbruteforce(checkhash, chars, 5, method = 'upto')
    print(list(key))
    r.clean()
    r.sendline(key)
    print(r.recvline(timeout=0.5))
print(r.clean(timeout=0.5))
```

#### Flag:flag{warm_casseroles_for_breakfast!!!}
