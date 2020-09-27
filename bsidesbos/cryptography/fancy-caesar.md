# Fancy Caesar

Didn't even look at the script but since the ciphertext is an array, we can guess that the flag is encrypted byte by byte. We bruteforce all 128 \(or so\) bytes and then get the flag. We also have to rot13 the flag before we get the actual flag.

## Flag: flag{meta\_flag\_is\_meta}

