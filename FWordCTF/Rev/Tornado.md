# Tornado 

Looking at the script, it scrambles the flag (by using one of the flag's characters as the seed), splits it into blocks of 2 bytes, and then pads them, and then AES encrypts them with a known key.

We start by decrypting each block with the key to get a long string: `aaFho_i_aC2b_abfc8edFw!kolae_ngbom_r__f_9T525eg__ihedd}{pmertt`

Then, we bruteforce the seed by trying each of the characters of the flag as the seed. We do this by scrambling our own string (I chose `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`) with the seed, and then comparing it to the above string and see if it's in flag format.

Seeing as "w" only appears once, and it is in the flag format, I based my check on this. We check if our output string[21] is equal to "B", since this is its place in the flag format.

We get our seed as "h", and we encrypt our string with it. Last thing to do is to match each character up to its original position. Script below:

#### Flag: FwordCTF{peekaboo_i_am_the_flag_!_i_am_the_danger_52592bbfcd8}

```py
a = "aaFho_i_aC2b_abfc8edFw!kolae_ngbom_r__f_9T525eg__ihedd}{pmertt"
b = "sUHoQmijkF23xd4568LEABgMCcNpqtuOPVWDhabT1Gyz0KefRSYZr79IJlvwXn"

a = list(a)
b = list(b)
c = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
o = ""
for i in range(len(a)):
  d = b.index(c[i])
  o += a[d]
print(o)
```
