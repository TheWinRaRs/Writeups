This was an RSA challenge where you had to break the prime generation function.
We see that the function
- Generates a 64 bit number
- Does a logical OR with 0xc000000000000001 on it
- Then, for 16 rounds:
  - Sets the chunk to s
  - Multiplies s by a constant a (0xe64a5f84e2762be5)
- Then, if the number generated is prime, it returns it

I got s1*s2 by getting the upper and lower bits of n and applying modinv

We can represent p as [x][xa][xa^2]... where each [] is 64 bits long or
p = x*64^15 + ax*64^14...

Multiplying it with q would give (kek how do i represent this)
[0 ][1 ][2 ]... ... [30][31] <- chunk indexes (64 bits long)
[xy    ]    ... ... [xya^30]
    [xya   ]... [xya^29]
    [xya   ]... [xya^29]
since its 
n = xy*64^30 + 2xya*64^30 ... + 2xya^29*64^1 + xya^30

We can get upper and lower bits of n to get upper and lower bits (with modinv of a) of xy like this.
however since theres a 2 coefficient on 2xya*64^30 this value is bit shifted and leaks into the last upper bits of xy. this gives 2 values what xy could be (one where the the bit is subtracted and one where it isnt). which are 0xab802dca026b182578adce5060bd0eb1 or 0xab802dca026b182478adce5060bd0eb1

Script below to gen s1*s2 (bit removal hasnt happened yet)
```python
def prinh(a):
    print(hex(a))

def cracc(n):
    upper = n >> (2048-128)
    u1 = upper >> 64
    lower = n % 2**65
    prinh(lower)

    a2 = pow(0xe64a5f84e2762be5,-1,2**65)
    for _ in range(30):
        lower = pow(lower*a2,1,2**65)
    prinh(lower)
    z = hex(u1)[-16:] + hex(lower)[-16:]

    return z
```
I factored these numbers and generated (kind of) all the 64 bit factors for both of these 128 bit numbers, and then tried using them as s in order to get the primes p and q.
0xab802dca026b182478adce5060bd0eb1 has no 64 bit factors, so it had to be 0xab802dca026b182578adce5060bd0eb1.
The 64 bit factors of that number are
[17323093358088416319, 11957115919933039605, 15301219884532198649, 14589535238740003363, 10091363333161070837, 14567509746395306455, 15648764542394866359, 15625139955456876315, 14898389259854230905, 14898389259854230905, 15625139955456876315, 15648764542394866359, 14567509746395306455, 10091363333161070837, 14589535238740003363, 15301219884532198649, 11642633479736017985, 9423396846760527157, 9883074741724455311, 13159516333377194255, 12330536802058217123]
I then modified the gen_prime function to, if it wasn't prime, don't repeat, since these s's should generate a prime without having to do anything. This resulted in the 2 factors p and q, and then we used this to decrypt the flag.
```python
import gmpy2
import math

a = 0xe64a5f84e2762be5
chunk_size = 64

def gen_prime(s):
     s |= 0xc000000000000001
     p = 0
     for _ in range(16):
       p = (p << chunk_size) + s
       s = a * s % 2**64
     if gmpy2.is_prime(p):
       return p


n = 0xab802dca026b18251449baece42ba2162bf1f8f5dda60da5f8baef3e5dd49d155c1701a21c2bd5dfee142fd3a240f429878c8d4402f5c4c7f4bc630c74a4d263db3674669a18c9a7f5018c2f32cb4732acf448c95de86fcd6f312287cebff378125f12458932722ca2f1a891f319ec672da65ea03d0e74e7b601a04435598e2994423362ec605ef5968456970cb367f6b6e55f9d713d82f89aca0b633e7643ddb0ec263dc29f0946cfc28ccbf8e65c2da1b67b18a3fbc8cee3305a25841dfa31990f9aab219c85a2149e51dff2ab7e0989a50d988ca9ccdce34892eb27686fa985f96061620e6902e42bdd00d2768b14a9eb39b3feee51e80273d3d4255f6b19
e = 0x10001
c = 0x6a12d56e26e460f456102c83c68b5cf355b2e57d5b176b32658d07619ce8e542d927bbea12fb8f90d7a1922fe68077af0f3794bfd26e7d560031c7c9238198685ad9ef1ac1966da39936b33c7bb00bdb13bec27b23f87028e99fdea0fbee4df721fd487d491e9d3087e986a79106f9d6f5431522270200c5d545d19df446dee6baa3051be6332ad7e4e6f44260b1594ec8a588c0450bcc8f23abb0121bcabf7551fd0ec11cd61c55ea89ae5d9bcc91f46b39d84f808562a42bb87a8854373b234e71fe6688021672c271c22aad0887304f7dd2b5f77136271a571591c48f438e6f1c08ed65d0088da562e0d8ae2dadd1234e72a40141429f5746d2d41452d916


bleh = [17323093358088416319, 11957115919933039605, 15301219884532198649, 14589535238740003363, 10091363333161070837, 14567509746395306455, 15648764542394866359, 15625139955456876315, 14898389259854230905, 14898389259854230905, 15625139955456876315, 15648764542394866359, 14567509746395306455, 10091363333161070837, 14589535238740003363, 15301219884532198649, 11642633479736017985, 9423396846760527157, 9883074741724455311, 13159516333377194255, 12330536802058217123]
for s in bleh:
  try:
    p = math.gcd(gen_prime(s),n)
    q = n//p
    tot = (p-1)*(q-1)
    d = pow(e,-1,tot)
    print(pow(c,d,n)) # long to bytes this after
  except:pass
```
#### `CTF{__donald_knuths_lcg_would_be_better_well_i_dont_think_s0__}`
