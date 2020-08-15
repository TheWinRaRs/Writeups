# Gambler

So the encryption calculates x^3 + ax + b mod p. Initially, we don't know a, b, or p, but we can encrypt arbitrary messages and get the encryption of the flag.

So, how do we leak values with this? First of all, we encrypt 0 - the equation will equate to b.

Next, we encrypt 1 - the equation will be 1 + a + b, so subtract b and subtract 1 to get a, or some value that equates to a mod p.

Finally, we must leak p. This is simple, continue encrypting small messages and also encrypting them ourselves with the calculated a and b values. Eventually, we'll find that our calculated value is different to the value returned - from there, we work out the modulus that would require both of the values to be equal. In my case, my calculated value was negative and the value returned by the server was positive so adding the absolute values returned the modulus.

This gives us the equation x^3 + ax + b mod p = c where we know a,b, and c. From there I got maf slave rak to solve the equation using sage :P

#### Flag: CCTF{__Gerolamo__Cardano_4N_itaLi4N_p0lYma7H}

No script because I did it all manually in a python prompt but here have my PoW solver

```py
from Crypto.Util.number import *

import os,hashlib,itertools
os.environ['PWNLIB_NOTERM'] = '1'

from pwn import *
from string import printable
printable = list(printable)
printable.remove('\n')
printable.remove('\x0b')
printable.remove('\x0c')
printable.remove('\t')
printable.remove(' ')
def powbuster(method,target,length):
    hash = eval(f"hashlib.{method}")
    for possible in itertools.combinations(printable,length):
        possible = ''.join(possible).encode()
        val = hash(possible).hexdigest()[-6:]
        if val == target:
            return possible
p = remote('05.cr.yp.toc.tf', 33371)
p.recvuntil(b"Please submit a printable string X, such that ")
method = p.recvuntil("(")[:-1].decode()
p.recvuntil("= ")
target = p.recvuntil(" ")[:-1].decode()
p.recvuntil("len(X) =")
length = int(p.recvline())
print(method,target,length)
ans = powbuster(method,target,length)
print(ans)
p.sendline(ans)
p.interactive()
```
