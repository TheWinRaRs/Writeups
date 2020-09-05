# Cheap Facades

So we get a file called flag.jpg but looking inside the hex shows png properties, Such as IHDR, IDAT, IEND etc etc.

So I overwrote the part of the file header that contained jpg with png.

After doing that I ran pngcheck on the file \(after renaming it to flag.png\) and it said thst the CRC of the image was 0 x 0, referring to the dimensions.

So I ran the script tony created for Dimensionless Loading and got \(\['\x00', '\x00', '\x01', '\xa4'\], \['\x00', '\x00', '\x00', 'E'\]\).

Here's the script:

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

Using this I overwrote the png bytes but again pngcheck said it was corrupt.

After this I didn't know what went wrong but it mentioned corruption errors.

Luckily I found a script that automatically fixes such errors though. This was called PCRT.py. After running this it opens the image and you get a flag of:

## Flag: ractf{D0n't\_judg3\_4\_f1le\_6y\_it5\_h34d3r}

