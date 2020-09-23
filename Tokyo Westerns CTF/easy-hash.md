# easy-hash

The hashing function takes a sum of the integer representation of 4 byte blocks. This means that the order of the blocks doesn't matter, we can just change the order of 2 of the blocks (that don't interfere with the other checks), and get a collision.

```bash
curl https://crypto01.chal.ctf.westerns.tokyo -d 'twctf: p givleasee me the flag of 2020'
```
#### Flag: TWCTF{colorfully_decorated_dream}
