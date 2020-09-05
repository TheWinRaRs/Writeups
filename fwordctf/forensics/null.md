# NULL

NULL

First of all, there are a few things in the header we need to fix. The first byte needs to be a 89, not a 69 \(nice\), and we need to capitalize the IHDR chunk header thing \(idk\)

Next, if we run a pngcheck, we see that the dimensions are 0x0. Thinking back to dimensionless loading, we can bruteforce the dimensions if the crc32 is intact.

```python
from zlib import crc32

data = open("NULL",'rb').read()
index = 12

ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11

for x in range(1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for i in range(len(height)):
            ihdr[height_index - i] = height[-i -1]
        for i in range(len(width)):
            ihdr[width_index - i] = width[-i -1]
        if hex(crc32(ihdr)) == '0xe3677ec0':
            print("width: {} height: {}".format(width.hex(),height.hex()))
    for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]
```

We then change the dimensions using something like GHEX: and then we can open the image as normal to get the flag.

## Flag: FwordCTF{crc32\_is\_the\_way}

