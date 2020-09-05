# Advanced Reversing Mechanics 2

Decompiling the file, we find it runs the encryptFlag function on the first argument, then prints the output out as hex.

The encrypt flag function runs some complicated airthmetic thing, which doesn't really matter that much, or at all.

What's notable is that the encryption is kind of a rolled byte by byte. That is, the same byte preceded by the same text before it will encrypt to the same thing.

Knowing the flag format, rgbCTF{flag}, we can use a byte by byte bruteforce.

I recreated the function inside of python and attempted to run the bruteforce there, but I got non-preferable results. So, I did this again, this time recreating the code in c and compiling it, then created a python wrapper script to run the bruteforce.

I'm not sure exactly why, but I had to constantly switch between the two scripts, using one to brute the next part of the flag, subbing it into the other to brute the next part of the flag, subbing that in... etc.

Anyhow after all of my pain and a little trial and error i was able to create the final flag.

Python script with recreation:

```python
import string
def encryptflag(toencrypt):
    index = 0
    bvvar3 = toencrypt[index]
    while True:
        curbyte = bvvar3
        uVar2 = curbyte - 10 & 0xff
        uVar4 = curbyte
        if (bvvar3 < 0x50) and (uVar4 == uVar2 or 0x50 < uVar2):
            uVar4 = curbyte + 0x46 & 0xff
        uVar4 = (uVar4 - 7 ^ 0x43) & 0xff
        pbVar1 = index + 1
        toencrypt[index] = (uVar4 << 6) | (uVar4 >> 2)
        bvvar3 = toencrypt[pbVar1]
        if bvvar3 == 0: break
        uVar4 = pbVar1 % 5
        bvvar3 = bvvar3 << (-uVar4 & 7) | bvvar3 >> (uVar4 & 0xff)
        if uVar4 == 2:
            bvvar3 = bvvar3 - 1
        toencrypt[pbVar1] = bvvar3
        bvvar3 = toencrypt[pbVar1]
        index = pbVar1
    for i in range(len(toencrypt)):
        toencrypt[i] = toencrypt[i] & 255
enc = [0x0A, 0xFB, 0xF4, 0x88, 0xDD, 0x9D, 0x7D, 0x5F, 0x9E, 0xA3, 0xC6, 0xBA, 0xF5, 0x95, 0x5D, 0x88, 0x3B, 0xE1, 0x31, 0x50, 0xC7, 0xFA, 0xF5, 0x81, 0x99, 0xC9, 0x7C, 0x23, 0xA1, 0x91, 0x87, 0xB5, 0xB1, 0x95, 0xE4]
flag = list(b"rgbCTF{ARM_ar1thm3t1c_r0cks_fad")
l = len(flag)
flag += [0]*(len(enc) - len(flag))
temparr = flag[:]
for i in range(l,len(enc)):
    for j in map(ord,string.ascii_lowercase + string.ascii_uppercase + '0123456789_}'):
        temparr = flag[:]
        temparr[i] = j
        encryptflag(temparr)
        if temparr[i] == enc[i]:
            flag[i] = j
            break
print(flag)
inter = map(chr,flag)
print(''.join(inter))
arr = list(b"rgbCTF{") + [0]
encryptflag(arr)
print(", ".join(map(hex,arr)))
```

Python script that used the binary I recompiled:

```python
import os
import string
from pwn import *
flag = "rgbCTF{ARM_ar1thm3t1c_r0cks_fad96"
enc = [0x0A, 0xFB, 0xF4, 0x88, 0xDD, 0x9D, 0x7D, 0x5F, 0x9E, 0xA3, 0xC6, 0xBA, 0xF5, 0x95, 0x5D, 0x88, 0x3B, 0xE1, 0x31, 0x50, 0xC7, 0xFA, 0xF5, 0x81, 0x99, 0xC9, 0x7C, 0x23, 0xA1, 0x91, 0x87, 0xB5, 0xB1, 0x95, 0xE4]
def getlast(string):
    response = os.popen(f"./arm {string}").read().split(", ")
    return int(response[-2],16)

for i in range(len(flag),len(enc)):
    for j in string.ascii_lowercase + string.ascii_uppercase + '0123456789_}':
        try:
            resp = getlast(flag + j)
            if resp == enc[i]:
                flag += j
                print(flag)
                break
        except:
            pass
    else:
        flag += '-'
print(flag.encode())

"""
for j in map(chr,range(256)):
    try:
        resp = getlast(flag + j)
        if resp == enc[len(flag)]:
            print(j)
    except:
        pass
"""
```

source of binary i recompiled:

```javascript
#include <stdlib.h>
#include <stdio.h>
#define true 1
void encryptFlag(char *flag);
int main(int param_1,char *argv[])
{
  char *pcVar1;
  char *pbVar2;
  char abStack272 [256];

  pcVar1 = stpcpy((char *)abStack272,argv[1]);
  encryptFlag(abStack272);
  pbVar2 = abStack272;
  for(int i = 0; i < strlen(argv[1]); i++){
    printf("%02X, ",(uint)((pbVar2[i] & 0xff)));
  }
  putchar(10);
  return 0;
}

void encryptFlag(char *flag)
{
  char *curpointer;
  char *pbVar1;
  uint uVar2;
  char bVar3;
  uint curbyte;
  uint uVar4;

  bVar3 = *flag;
  curpointer = flag;
  if (bVar3 == 0) {
    return;
  }
  while( 1) {
    curbyte = (uint)bVar3;
    uVar2 = curbyte - 10 & 0xff;
    uVar4 = curbyte;
    if ((bVar3 < 0x50) && (uVar4 = uVar2, 0x50 < uVar2)) {
      uVar4 = curbyte + 0x46 & 0xff;
    }
    uVar4 = (uVar4 - 7 ^ 0x43) & 0xff;
    pbVar1 = curpointer + 1;
    *curpointer = (char)(uVar4 << 6) | (char)(uVar4 >> 2);
    bVar3 = *pbVar1;
    if (bVar3 == 0) break;
    uVar4 = (int)(pbVar1 + -(int)flag) % 5;
    bVar3 = bVar3 << (-uVar4 & 7) | bVar3 >> (uVar4 & 0xff);
    if (uVar4 == 2) {
      bVar3 = bVar3 - 1;
    }
    *pbVar1 = bVar3;
    bVar3 = *pbVar1;
    curpointer = pbVar1;
  }
  return;
}
```

## Flag: rgbCTF{ARM\_ar1thm3t1c\_r0cks\_fad961}

