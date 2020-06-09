# Dimensionless Loading

We're given a PNG with the size fields set to 0. However, the CRC is intact, and we can 'crack' the original dimensions with this.


```python
from zlib import crc32
from pwn import p32

target = 0x5b8af030
header = "49 48 44 52 00 00 00 99 00 00 00 99 08 06 00 00 00".replace(' ', '').decode('hex')
def check_size(w,h, header):
        w = p32(w)[::-1]
        h = p32(h)[::-1]
        header = header.replace("\x00\x00\x00\x99" + "\x00\x00\x00\x99", w+h)
        if crc32(header) == target:
                print(list(w),list(h))

for x in range(2000):
        for y in range(2000):
                check_size(x,y,header)
```
Sizes are: 0x00 0x00 0x05 0x62
0x00 0x00 0x01 0x6B

#### ractf{m1ss1ng_n0_1s_r34l!!}
