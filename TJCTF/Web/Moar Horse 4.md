# Moar Horse 4

Jwt HSA/RSA signing vulnerability
Use pubkey.pem with jwt_tool.py
'speed' is calculated with  
```python
speed = int(hashlib.md5(("Horse_" + horse).encode()).hexdigest(), 16)
```
'ajuuer' is fast enough
Set horses to ["ajuuer"]  
Race  
Get flag  
#### tjctf{w0www_y0ur_h0rs3_is_f444ST!} 
```python
from pwn import *
import hashlib
from pwnlib.util.iters import mbruteforce
import string

BOSS_HORSE = "MechaOmkar-YG6BPRJM"
goal = int(hashlib.md5(("Horse_" + BOSS_HORSE).encode()).hexdigest(), 16)
def attempt(horse):
        speed = int(hashlib.md5(("Horse_" + horse).encode()).hexdigest(), 16)
        if speed > goal:
                return True
        else:
                return False
myhorse = mbruteforce(attempt, string.ascii_lowercase, length=10)
print(myhorse)
```
