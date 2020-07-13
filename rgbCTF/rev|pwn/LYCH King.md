# LYCH King

So with some experimentation we found the binary actually XORs the inputted plaintext with a one time pad. Just sub in the ciphertext right? Kind of?

If we sub in a plaintext we know and xor back to get the stream we get a bunch of numbers. With a bit of help from the author and some research we realised these numbers were a sequence of lychrel numbers. The first bit of the stream, 1997, is a lychrel number, specifically the seed stored inside of the binary which it then uses to generate the rest of the lychrel, converts to string and then XORs.

"the bad seed" implies this seed must be fixed.

Soooo i just found out the position in the binary the seed was stored(0x7c5b) and bruteforced the seed in that location. Grepping for rgb gives us the plaintext

He&jaeden created the Lich King ages ago from the spirit of the orc shaman Ner'zhul to raise an undead army to conquer Azeroth for the Burning Legion. rgbctf{the flag is just rgb lol} Initially trapped within the Frozen Throne with Frostmourne, the Lich King eventually betrayed Kil'jaeden and merged with the human Arthas Menethil. When Frostmourne was destroyed and Arthas perished, Bolvar Fordragon became the new Lich King, imprisoning the master of the Scourge within the Frozen Throne once more in order to protect the world from future threats.:

Which yields the flag.
```python
from pwn import *
ciphertext = open("cipher","rb").read()
def xor(bytes1,bytes2):
    return bytes(b1 ^ b2 for b1,b2 in zip(bytes1,bytes2))
def decryptstring(seed):
    f = open("lich","r+b")
    f.seek(0x7c5b)
    f.write(p32(seed))
    f.close()
    output = os.popen(f"./lich {'a'*len(ciphertext)}").read().encode()
    stream = xor(output,b'a'*len(ciphertext))
    return xor(ciphertext,stream)
for i in range(1,5000):
    print(decryptstring(i))
```

#### Flag: rgbctf{the flag is just rgb lol}
