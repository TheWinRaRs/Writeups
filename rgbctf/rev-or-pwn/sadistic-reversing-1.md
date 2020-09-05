# Sadistic Reversing 1

Input is taken, something is done to it, and it outputs a list of transformed chars as ascii. We're given a goal string, and by entering 'rgbCTF{' we can see the initial numbers match up. So brrrrrutefoce go brrrr

```python
from pwn import *

goal = [114, 20, 119, 59, 104, 47, 75, 56, 81, 99, 23, 71, 56, 75, 124, 31, 65, 32, 77, 55, 103, 31, 96, 18, 76, 41, 27, 122, 29, 47, 83, 33, 78, 59, 10, 56, 15, 34, 94]
outs = "rgbCTF{"
import string, subprocess
chars = string.printable
while True:
    currentgoal = repr(goal[:len(outs)+1])
    for c in chars:
        process = subprocess.Popen(['./itJX.so', outs+c], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if currentgoal in out:
            outs += c
            print(outs)
            break
```

## rgbCTF{th1s\_pr0bably\_w@s\_d1ff1cult6362}

