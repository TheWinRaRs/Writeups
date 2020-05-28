# Wacko Images

![text](https://github.com/TheWinRaRs/Writeups/blob/master/Angstrom/Wacko%20Images/enc.png) ![text](https://github.com/TheWinRaRs/Writeups/blob/master/Angstrom/Wacko%20Images/flag.png)

We have ab mod c = d where we know b (key), c (251), and d (encrypted pixel value).
Multiplying by the modular inverse of b gets us:
a mod c = d * b^-1 mod c

Calculate this for every pixel in the image with a script, and you get an image that contains the flag.

```py
import numpy as np
from PIL import Image
from Crypto.Util.number import inverse

enc_image = Image.open('enc.png')
img = np.array(enc_image)

a, b, c = img.shape

key = [41, 37, 23]

for x in range(0, a):
    for y in range(0, b):
        pixel = img[x, y]
        for i in range(0, 3):
            pixel[i] = inverse(key[i], 251) * pixel[i] % 251
        img[x, y] = pixel

flag = Image.fromarray(img)
flag.save('flag.png')
```

The flag is:
#### actf{m0dd1ing_sk1llz}
