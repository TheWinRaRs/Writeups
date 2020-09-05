# Satan's jigsaw

We can unpack the 7zip to get a large amount of jpg image files - 90,000 image files to be precise. Each image file contains one pixel, and one pixel only. From the challenge briefing, we can tell that we need to somehow assemble these pictures to get an image.

The problem is, we have no way to know how to assemble it.

Each image is named something like this: `<number>.jpg` . Given the hint, I decided to use the python crypto library's long\_to\_bytes to turn all of the numbers into byte strings. What i found was that each of the names, when turned into byte strings, held the position of that pixel in the form

`x y`

I wrote a script using PIL to go through all of the images, get the position of the pixel they represent, and then construct the flag image.

The resulting image has two QR codes. The one on the upper left appears to be a rick roll, however the one on the bottom right yields the flag.

![pencil qr](https://media.discordapp.net/attachments/699999846119243857/703576030417518602/flag.jpg)

```python
from PIL import Image
from Crypto.Util.number import long_to_bytes
import os, re
from numpy import *
flag = zeros((300,300,3), dtype='uint8')
files = os.listdir("chall")
files = list(filter(lambda x: 'jpg' in x, files))
fullfiles = list(map(lambda x: 'chall/' + x, files))
jpg = bytes([0xff,0xd8,0xff])
positions = []
for file in files:
    pos = long_to_bytes(int(re.findall("(.*).jpg", file)[0])).decode().split()
    pos = list(map(int, pos))
    positions.append(pos)
for i,pos in enumerate(positions):
    img = Image.open(fullfiles[i])
    img = array(img)
    pixel = img[0,0]
    flag[pos[0]][pos[1]] = pixel
dec = Image.fromarray(flag)
dec.save("flag.jpg")
```

## rtcp{d1d-you\_d0\_7his\_by\_h4nd?}

