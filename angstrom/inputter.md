# Inputter

Look at the source code, gives you the arguments that you need to put into the program, and what you must type in the buffer. They are unprintable characters, so use a python script to run it

```python
from PIL import Image
temp = 0
im = Image.open('breathe.jpg', 'r')
im2 = Image.open('output.png', 'r')
pix_val = list(im.getdata())
pix_val2 = list(im2.getdata())
flag = []
pix_list = zip([x for sets in pix_val for x in sets], [x for sets in pix_val2 for x in sets])
for i in pix_list:
    if len(str(i[1])) < len(str(i[0])):
        temp *= 10
    elif i[1] == 255:
        temp *= 10
    else:
        temp = (temp*10)+int(str(i[1])[0])
    if len(str(temp)) == 3:
        flag.append(chr(temp))
        temp = 0
    elif len(str(temp)) == 2 and temp != 11 and temp != 12 and temp != 10:
        flag.append(chr(temp))
        temp = 0
print("".join(flag))
```

## actf{inhale\_exhale\_ezpz-12309biggyhaby}

