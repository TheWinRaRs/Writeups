# Amsterdam

just some rev

1. reverse with base 3
2. find K and N \(ez\)
3. undo adding

b'..:: CCTF{With\_Re3p3ct\_for\_Sch4lkwijk\_dec3nt\_Encoding!} ::..'

## Flag: CCTF{With\_Re3p3ct\_for\_Sch4lkwijk\_dec3nt\_Encoding!}

Scripts:

```python
#!/usr/bin/env python3

from Crypto.Util.number import *
from functools import reduce
import operator
#from secret import flag, n, k

def comb(n, k):
    if k > n :
        return 0
    k = min(k, n - k)
    u = reduce(operator.mul, range(n, n - k, -1), 1)
    d = reduce(operator.mul, range(1, k + 1), 1)
    return u // d 

comb(5,2)
def encrypt(msg, n, k):
    msg = bytes_to_long(msg.encode('utf-8'))
    if msg >= comb(n, k):
        return -1
    m = ['1'] + ['0' for i in range(n - 1)]
    for i in range(1, n + 1):
        if msg >= comb(n - i, k):
            m[i-1]= '1'
            msg -= comb(n - i, k)
            k -= 1
    m = int(''.join(m), 2)
    i, z = 0, [0 for i in range(n - 1)]
    c = 0
    while (m > 0):
        if m % 4 == 1:
            c += 3 ** i 
            m -= 1
        elif m % 4 == 3:
            c += 2 * 3 ** i
            m += 1
        m //= 2
        i += 1
    return c

enc = encrypt(flag, n, k)
print('enc =', enc)
```

Output:

```text
enc = 5550332817876280162274999855997378479609235817133438293571677699650886802393479724923012712512679874728166741238894341948016359931375508700911359897203801700186950730629587624939700035031277025534500760060328480444149259318830785583493
```

Script 2:

```python
from Crypto.Util.number import *
from functools import reduce
import operator

def comb(n, k):
    if k > n :
        return 0
    k = min(k, n - k)
    u = reduce(operator.mul, range(n, n - k, -1), 1)
    d = reduce(operator.mul, range(1, k + 1), 1)
    return u // d 

def from_int(num, base, alpha="0123456789abcdef"):
    out = ""
    while num:
        out = alpha[num%base] + out
        num //= base
    return out or alpha[0]

ct = 5550332817876280162274999855997378479609235817133438293571677699650886802393479724923012712512679874728166741238894341948016359931375508700911359897203801700186950730629587624939700035031277025534500760060328480444149259318830785583493
#     5550332948208120629025411001331320743912337889071945074153769995654439069135971336244981001925727908903742116646762141899301774026507397497025053737665676875918569586865903953910920954499256359219273488814885412340248767805295663882248
ct = from_int(ct,3)
print(ct)
m = 0
for i in ct:
    m *= 2
    if i == "1":
        m += 1
    elif i == "2":
        m -= 1


print(m)

c = [i for i in from_int(m,2)]#[1:]
n = len(c)#+1
k = 0
for i in c:
    if i == "1":
        k += 1

print(n,k)

msg = -comb(n - 1, k)

for i in range(1, n + 1):
    if c[i-1] == '1':
        msg += comb(n - i, k)
        k -= 1

print(long_to_bytes(msg))
```

