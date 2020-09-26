Now we didn't *actually* solve this, due to instability with the challenge. But we came up with a script that seemed to be working well before the instance died:

```py
from pwn import *
import random

regex1 = [str(i) for i in range(100, 1000)]
regex2 = [i * 5 for i in 'abcdefghijklmnop']
regex3 = ['1.' + '1'*i for i in range(1, 1000)]
regex4 = ['+' + '1'*i for i in range(3, 1000)]
regex5 = ['<' + 'a'*i + '>' for i in range(1, 1000)]
regex6 = [f'0{i}:{j}' for i in range(10) for j in range(60)]
regex7 = [f'1{i}-01-{j}' for i in range(100, 1000) for j in range(10, 30)]
regex8 = ['a'*i + '@a.com' for i in range(1, 200)]
regex9 = ['https://www.youtube.com/channel/UC' + i + j + 20*k + '/' for i in 'abcdefghijklmnopq' for j in 'abcdefghijklmnopq' for k in 'abcdefghijklmnopq']
regexA = [' '.join(['.....']*i) for i in range(1, 200)]
regexB = ['1.1.1.' + str(i) for i in range(256)]
regexC = ['0'*i for i in range(1, 100)]
regexD = ['00' + '::'*i for i in range(1, 200)]

r = remote("challenge.ctf.games", 30811)
while True:
    r.recvuntil('?\n')
    regex = r.recvline().strip().decode()

    if regex == '^\d{3}$':
        pwned = regex1.pop()
    elif regex == '^\w{5}$':
        pwned = regex2.pop()
    elif regex == '^\d*\.\d+$':
        pwned = regex3.pop()
    elif regex == '^\+?(\d.*){3,}$':
        pwned = regex4.pop()
    elif regex == '<\/?[\w\s]*>|<.+[\W]>':
        pwned = regex5.pop()
    elif regex == '^(0?[1-9]|1[0-2]):[0-5][0-9]$':
        pwned = regex6.pop()
    elif regex == '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))':
        pwned = regex7.pop()
    elif regex == '^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$':
        pwned = regex8.pop()
    elif regex == 'https?:\/\/(www\.)?youtube.com\/channel\/UC([-_a-z0-9]{22})/':
        pwned = regex9.pop()
    elif regex == '^[.-]{1,5}(?:[ \\t]+[.-]{1,5})*(?:[ \\t]+[.-]{1,5}(?:[ \\t]+[.-]{1,5})*)*$':
        pwned = regexA.pop()
    elif regex == '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$':
        pwned = regexB.pop()
    elif regex == r'^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?$':
        pwned = regexC.pop()
    elif regex == r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))':
        pwned = regexD.pop()
    else:
        print(f"Error couldn't find valid regex for {regex}")

    log.success("Regex: " + regex)
    log.success("Generated: " + pwned)

    r.recvuntil('> ')
    r.sendline(pwned)
    ```
