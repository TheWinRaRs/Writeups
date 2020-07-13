# Adequate Encryption Standard

Let's break down the encryption step by step.

It splits the plaintext into padded blocks of 8. It also expands the key using a key expansion function so that the key is as long as the amount of blocks. The key expansion function causes a drastic loss in size of the keyspace by using modular exponentiation that is not with primitive roots and is modulus a composite(256), which would allow for more optimised bruteforce, but I didn't use this in the end. For each block, it goes through 8 rounds. In each round:
1. Take the current ciphertext. Put it through the sbox(basically a substitution table)
2. Then, put it through the pbox, essentially shuffling the binary based on a pre-determined pbox of indexes.
3. Xor every byte of the current block with the current byte of the expanded key

The sbox and the pbox are things we can easily invert. The only real "encryption" step is the xor bit.

The problem is that unlike normal AES where the key is expanded into 11 keys of the same length of the blocks, in here the key is expanded into essentially 1 byte keys. For each block, for each round, it will keep XORing with the same current byte of the key.

Essentially, we can bruteforce each byte of the key until we get printable values, as the encryption reduces the key in each block to one byte, and this one byte can be bruteforced.

I wrote inversion functions to handle the sbox and pbox, then simply bruted the one byte expanded key of each block until I got a printable value. We can concatenate the decrypted blocks to get the flag,

Script:
```python
from Crypto.Util.number import *
import string
BLOCK_SIZE = 8
ROUNDS = 8
import base64
sbox = [111, 161, 71, 136, 68, 69, 31, 0, 145, 237, 169, 115, 16, 20, 22, 82, 138, 183, 232, 95, 244, 163, 64, 229, 224, 104, 231, 61, 121, 152, 97, 50, 74, 96, 247, 144, 194, 86, 186, 234, 99, 122, 46, 18, 215, 168, 173, 188, 41, 243, 219, 203, 141, 21, 171, 57, 116, 178, 233, 210, 184, 253, 151, 48, 206, 250, 133, 44, 59, 147, 137, 66, 52, 75, 187, 129, 225, 209, 191, 92, 238, 127, 241, 25, 160, 9, 170, 13, 157, 45, 205, 196, 28, 146, 142, 150, 17, 39, 24, 80, 118, 6, 32, 93, 11, 216, 220, 100, 85, 112, 222, 226, 126, 197, 180, 34, 182, 37, 148, 70, 78, 201, 236, 81, 62, 42, 193, 67, 8, 164, 43, 252, 166, 221, 208, 176, 235, 149, 109, 63, 103, 223, 65, 56, 140, 255, 218, 54, 153, 2, 228, 1, 240, 248, 246, 110, 156, 60, 227, 207, 254, 51, 174, 79, 128, 155, 251, 242, 177, 135, 230, 154, 179, 15, 189, 143, 130, 27, 107, 211, 30, 105, 19, 134, 124, 125, 245, 76, 204, 12, 26, 38, 40, 131, 117, 87, 114, 213, 212, 102, 195, 101, 55, 10, 47, 120, 200, 217, 88, 83, 36, 198, 249, 192, 23, 94, 181, 73, 185, 172, 165, 58, 53, 202, 106, 5, 7, 175, 89, 72, 90, 14, 162, 158, 119, 139, 77, 108, 190, 91, 29, 49, 159, 33, 113, 214, 4, 123, 199, 167, 35, 239, 84, 3, 132, 98]
pbox = [39, 20, 18, 62, 4, 60, 19, 43, 33, 6, 51, 61, 40, 35, 47, 16, 23, 58, 31, 53, 28, 55, 54, 30, 17, 42, 34, 45, 49, 13, 46, 0, 26, 2, 8, 3, 11, 48, 63, 36, 37, 7, 32, 5, 27, 59, 29, 44, 14, 56, 21, 22, 12, 52, 57, 41, 10, 1, 24, 38, 50, 15, 9, 25]
def to_blocks(in_bytes: bytes) -> list:
    return [in_bytes[i:i + BLOCK_SIZE] for i in range(0, len(in_bytes), BLOCK_SIZE)]
def invert_sbox(in_bytes: bytes):
    return bytes([sbox.index(b) for b in in_bytes])
def invert_pbox(in_bytes: bytes):
    permuted = ''.join(bin(b)[2:].zfill(8) for b in in_bytes)
    binary = list('-'*BLOCK_SIZE*8)
    for i in range(len(permuted)):
        binary[pbox[i]] = permuted[i]
    binary = ''.join(binary)
    return long_to_bytes(int(binary,2))
def decwithbyte(block,byte):
    for _ in range(ROUNDS):
        block = bytearray(block)
        for i in range(len(block)):
            block[i] ^= byte
        block = invert_pbox(block)
        block = invert_sbox(block)
    return block
enc = base64.b64decode(b"hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg==")
enc = to_blocks(enc)
flagregex = string.printable
flag = ''
for block in enc:
    for i in range(256):
        try:
            response = decwithbyte(block,i)
            response = response.decode()
            if all(x in flagregex for x in response):
                flag += response
                break
        except:
            pass
print(flag)
```

#### Flag: rgbCTF{brut3_f0rc3_is_4LW4YS_th3_4nsw3r(but_with_0ptimiz4ti0ns)}
