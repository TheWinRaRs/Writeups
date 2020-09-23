# sqrt

script does rsa but uses a power of 2 instead of a normal e, and uses a prime as n.

so, basically it does pow(pt,2**64,p)

this is somewhat reversible, since we can take the modular square root of the ct repeatedly until we get our plaintext.

one problem though - there are 2 modular square roots

this means that we would potentially have to go through 2**64 roots in order to get the correct one

we can reduce this significantly by finding the "pseudo-phi", which we can just use Crypto.Util.number's inverse for

this finds pow(pt,2**30,p)

this is significantly lower, and this is feasible to bruteforce

i didnt solve so i dont have script but uhhhhhh yeah
