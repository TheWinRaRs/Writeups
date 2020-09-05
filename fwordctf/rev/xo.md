# XO

Whatever we input, the binary searches for characters in our input that are the same as a character of the flag in the same position. It prints the number of characters before the first occurrence of this. For example, if the flag was FwordCTF{}, then...

Fgjehrfd -&gt; 0

sws -&gt; 1

gggg -&gt; 4

Using this, we can run a simple byte by byte bruteforce in order to get the data in flag.txt - NuL1\_Byt35?15\_IT\_the\_END?Why\_i\_c4nT\_h4ndl3\_That!}

Adding the flag format, we get the flag, FwordCTF{NuL1\_Byt35?15\_IT\_the\_END?Why\_i\_c4nT\_h4ndl3\_That!}

I used backticks for padding since they were pretty much guaranteed not to be in the flag - we can send backtick\_padding + char and bruteforce "char" until the number returned equals the number of backticks, the character of the flag in that position would be the char where the server returned number is equal to the number of backticks.

## Flag: FwordCTF{NuL1\_Byt35?15\_IT\_the\_END?Why\_i\_c4nT\_h4ndl3\_That!}

```python
from pwn import *
import time
printable = "?_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*(){},./<~\\"
host = ('xo.fword.wtf', 5554)
def getnum(string):
    while True:
        try:
            p = remote(*host)
            break
        except socket.gaierror:
            time.sleep(1)
    #p = process("./task")
    p.recvline()
    p.sendline(string)
    ans = int(p.recvline())
    p.close()
    return ans
flag = ''
i = len(flag)
while '}' not in flag:
    pad = '`'*i 
    for char in printable:
        totry = pad + char
        print(totry)
        if getnum(totry) == i:
            flag += char
            print(f"Flag: {flag}")
            break
    else:
        print(flag)
        quit()
    i += 1
```

