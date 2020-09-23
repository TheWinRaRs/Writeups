# Twin D

From the script, we can produce the following equations e1 \* d = 1 mod phi e2 \* \(d + 2\) = 1 mod phi

Rearranging e1 \* d = 1 mod phi e2 \* d + e2 \* 2\) = 1 mod phi

Then, we subtract e2\*2 from 1 to get e1 \* d = 1 mod phi e2 \* d = some negative number

We then can do a trick I learnt from FwordCTF \(kinda\)

We multiply both equations by the opposite value to get

e1 \* d \* e2 = e2 e1 \* e2 \* d = some negative number \* e1

Now we know that these are both the same, so we can simply subtract them from each other to get a multiple of phi.

If we know k\*phi, we can just use that as phi, since that will still work. We use this then to get the flag.

Solve script below.

## Flag: TWCTF{even\_if\_it\_is\_f4+e}

```text
from Crypto.Util.number import long_to_bytes

n = [value]
e1 = [value]
e2 = [value]
enc = [value]

e_2 = 1 - (2*e2)
# now we have e1 * d and e2 * d

e_1 = e2 # since e1 * d = 1
e_2 = e_2 * e1

tot = e_2 - e_1
d = pow(e1,-1,tot)
pt = pow(enc,d,n)

print(long_to_bytes(pt))
```

