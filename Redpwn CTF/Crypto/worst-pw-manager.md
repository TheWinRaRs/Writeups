# worst-pw-manager

the rc4 alg is perfect and works as intended however the key gen is flawed
```python
def generate_key():
    key = [KeyByteHolder(0)] * 8 # TODO: increase key length for more security?
    for i, c in enumerate(take(flag, 8)): # use top secret master password to encrypt all passwords
        key[i].num = c
    return key
```
As you can see in python it multiplies the key by 8 which from when i learned from making my maze alg, means changing one val changes all of the others at the same time. this creates a key thats 8 repeats of the same char. i brute forced this and checked it to get the correct char.

the output gives repeat of 
fptd_ics_htaopps}ysnnp{idtsltu_idr_aoug_iy_ 
and creates

#### flag{crypto_is_stupid_and_python_is_stupid}
