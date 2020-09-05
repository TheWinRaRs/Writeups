# B007l3G CRYP70

By uh... guessing?

we figure out that encoding method is:

-taking the ord value of the char

-subtracting it from 255

-generating 4 numbers that add to this number

This can be reversed easily with this script:

```python
#script that will error but give flag
a = "41 36 37 27 35 38 55 30 40 47 35 34 43 35 29 32 38 37 33 45 39 30 36 27 32 35 36 52 72 54 39 42 30 30 58 27 37 44 72 47 28 46 45 41 48 39 27 27 53 64 32 58 43 23 37 44 32 37 28 50 37 19 51 53 30 41 18 45 79 46 40 42 32 32 46 28 37 30 43 31 26 56 37 41 61 68 44 34 26 24 48 38 50 37 27 31 30 38 34 58 54 39 30 33 38 18 33 52 34 36 31 33 28 36 34 45 55 60 37 48 57 55 35 60 22 36 38 34"

b = a.split(" ")
o = ""
for i in range(len(a)//4):
  c = i * 4
  d = int(b[c]) + int(b[c+1]) + int(b[c+2]) + int(b[c+3])
  e = 255 - d
  o += chr(e)
  print(o)
```

## Flag: ractf{d0n7\_r0ll\_y0ur\_0wn\_cryp70}

