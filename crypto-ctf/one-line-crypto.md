# One Line Crypto

bruteforce X using m counting down

```python
candidates = set()

x = 1
m = 160
while True:
    while (x**(m+1) - (x+1)**m).bit_length() < 1023:
        x += 1
    while (num := x**(m+1) - (x+1)**m).bit_length() < 1026:
        if isPrime(num):
            for i in candidates:
                if min(i, num) < max(i, num) < min(i, num) << 3 and (i*num).bit_length() == 2048:
                    phi = (i-1)*(num-1)
                    d = inverse(0x10001, phi)
                    pt = pow(flag, d, i*num)
                    try:
                        print(long_to_bytes(pt).decode())
                        quit()
                    except Exception:
                        pass
            candidates.add(num)                                                                                                                                                                         
        x += 1                                                                                                     
    m -= 1
```

