# Flagdroid
Android Smali Rev - it reads flag{(.*)} then splits by _, checking each part
1st part - references a b64 string in resources

dEg0VA== - tH4T

2nd part - Does a wacky algorithm here's my solver
```py
result = [hex(ord(x)) for x in "\x1f\x54\x54\x3a\x1f\x35\xf1\x48\x47"]
start = "hack.lu20"

def calculate(inp):
    res = [ord(x) for x in inp]
    for i,v in enumerate(inp):
        res[i] += i
        res[i] ^= ord(start[i])
    res = [hex(x) for x in res]
    return res

import string
found = ''
for c in range(0, 9):
    for char in string.printable:
        res = calculate(found + char)
        if res[c] == result[c]:
            found += char
            print(found)
            break
```
2: w45N-T~so

3 - ``!var1.substring(0, 4).equals("h4rd") ? false : md5(var1).equals("6d90ca30c5de200fe9f671abb2dd704e");``

Takes an 8 char string and md5s it. We're given the first four chars
```bash
.\hashcat.exe -m 0 -a 3 ..\hash.txt h4rd?a?a?a?a
```
3: h4rd~huh

4 - It calls `return var1.equals(this.stringFromJNI());`

I found it loads a custom library which exports this function. It basically just mallocs a small area then pushes some data into it

Final solution:

#### Flag: flag{tH4T_w45N-T~so_h4rd~huh_0r~w4S-1t?8)}
