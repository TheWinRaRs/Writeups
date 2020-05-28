# Taking Off

Found arguments were 3 numbers 0-9 and "chicken"
Although not meant to I brute forced it with this python script:  
```python
import itertools
import os

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for c in itertools.product(nums, repeat=3):
    args = "(echo " + str(c[0]) + "; echo " + str(c[1]) + "; echo " + str(c[0]) + ") | ./taking_off"
    args = "./taking_off " + str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " chicken"
    print(args)
    os.system(args)
```
String `"ZFOKYO\nMC\O\nLFKM"` seen in memory
About where the password is compared
XOR it with the key 2a to get 'please give flag' with newlines removed.
