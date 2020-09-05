# Tyrannosaurus Rex

So the encryption takes some data, then base64 encodes it and encrypts it by XORing each byte with the byte after it, wrapping the last byte around to the start. The result is then hexlified. So, we can simply bruteforce the first byte in order to bruteforce what the decryption is. This gives us the base64 of the flag, which can be base64 decoded to get:

## Flag: flag{tyrannosauras\_xor\_in\_reverse}

