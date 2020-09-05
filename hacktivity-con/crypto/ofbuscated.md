# OFBuscated

So, from the title, we guess it's using OFB encryption.

For those of you that don't know, OFB encryption works like this: Firstly, like any AES mode, there is a key, and then with OFB, you also have an IV. Then:

* Encrypt the IV using the key
* Sets the new IV to the encrypted IV
* Xor the plaintext block with the encrypted IV, and then this is the output

This repeats for each block.

After reading the script, we can work out that:

* It takes the flag.txt, and reads this
* Pads this data using pkcs7 padding
* Splits the data into blocks of 16 bytes
* Randomly shuffles these blocks
* Encrypts the blocks with the OFB we mentioned above.

Since the IV and key stay constant, we can connect and receive as many data samples as we want, and since there are 3 blocks, there are only 6 possible permutations for the blocks to be in. \(doesn't really matter but whatever\)

Looking even closer at the script, we see this line:

```python
assert len(flag) % 16 == 1
```

This means that the length of the flag must be 33, as we have already established that there are three blocks. This also means, because of the way the data is padded, that one of the blocks must be `"}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"` \(we know the last char is "}"\)

Now, we can simply attempt to XOR each block with this string to get the key for that block, and then XOR that with the other blocks to get the flag. I made this table for convenience.

```text
block\position:   1                                 2                            3
1 e92c6ede25edd6694b4de6f9565624d2  7e4cdcceda0a5284178d43205b448d35 24d20b9d166edb74bb80fa7ddf96d6a7
2 fb1f66cd01ffcc75787bfbd27d4d22cd  771cbab58a7528e774dd255b0b27ed56 36e1038e327cc16888b6e756f48dd0b8
3 f24f00b65180b6161b2b9da92d2e42ae  652fb2a6ae6732fb47eb3870203ceb49 3fb165f56203bb0bebe6812da4eeb0db
```

We then XOR f24f00b65180b6161b2b9da92d2e42ae with 7d0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f to get 8f400fb95e8fb919142492a622214da1, which is what XOR key was used to encrypt the first block.

Then, we simply XOR this key with each of the other blocks to get the rest of the flag.

```text
e92c6ede25edd6694b4de6f9565624d2 ^ 8f400fb95e8fb919142492a622214da1 = 666c61677b626f705f69745f74776973 = flag{bop_it_twis
fb1f66cd01ffcc75787bfbd27d4d22cd ^ 8f400fb95e8fb919142492a622214da1 = 745f69745f70756c6c5f69745f6c6f6c = t_it_pull_it_lol
f24f00b65180b6161b2b9da92d2e42ae ^ 8f400fb95e8fb919142492a622214da1 = 7d0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f = }...............
```

## Flag: flag{bop\_it\_twist\_it\_pull\_it\_lol}

