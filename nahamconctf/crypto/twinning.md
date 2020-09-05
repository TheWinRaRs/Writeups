# Twinning

easy RSA

factor the numbers

```python
>>> from Crypto.Util.number import *
>>> phi = (2256911-1)*(2256913-1)
>>> n = 5093651775743
>>> e = 65537
>>> d = inverse(e, phi)
>>> ct = 3084160692905
>>> pow(ct, d, n)
6444
>>>
```

## flag{thats\_the\_twinning\_pin\_to\_win}

