# ECB is the best CB

We can run a "chosen plaintext" attack on the server. It takes our input, then calculates encrypt(input + flag). Because ECB encrypts each block separately and simply concatenates them, we can brute force the flag byte by byte.
A block is 16 bytes. Say if we gave the server 15 As, This means that the first block of the response is the ECB encryption of 15 As + the first byte of the flag. We'll call this block k1.

If we continuously send 15 As + <test byte> and then compare the first block, then the byte in which the first block of the encryption is equal to k1 is the first byte of the flag.

If we send 14 As, the first block is the encryption of 14As plus the first two bytes of the flag. given the first byte of the flag, we can run a similar brute force. This continues for the first block, the second block, and however many blocks there are until the flag finishes.
