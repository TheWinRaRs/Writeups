# comprehensive2

```python
a = [1, 18, 21, 18, 73, 20, 65, 8, 8, 4, 24, 24, 9, 18, 29, 21, 3, 21, 14, 6, 18, 83, 2, 26, 86, 83, 5, 20, 27, 28, 85, 67, 5, 17, 2, 7, 12, 11, 17, 0, 2, 20, 12, 26, 26, 30, 15, 44, 15, 31, 0, 12, 46, 8, 28, 23, 0, 11, 3, 25, 14, 0, 65]
print(str([x for z in [[[ord(m[i]) ^ ord(n[j // 3]) ^ ord(n[i - j - k]) ^ ord(n[k // 21]) for i in range(j + k, j + k + 3)] for j in range (0, 21, 3)] for k in range(0, len(m), 21)] for y in z for x in y])[1:-1])
#i deobfuscated first to get
for k in range(0, 63, 21):
    for j in range (0, 21, 3):
        for i in range(j + k, j + k + 3): # every 3 char chunks
            shat = ord(m[i])
            #shat = a[i] i will use this later to solve
            shat ^= ord(n[j // 3]) #[0,1... 6]
            shat ^= ord(n[i - j - k]) #[0,1,2]
            shat ^= ord(n[k // 21]) #[0,1,2]
            go += chr(shat)
print(go)
#then i made this script to find where the flag could be
for i in range(0,60,3):
    crib = " tjctf{"
    for j in range(2):
        for k in range(3):
            pp = a[i:i+6]
            x = pp[0+j] ^ pp[1+j] ^ pp[3+j] ^ pp[4+j]
            x^= ord(crib[0+k]) ^ ord(crib[1+k]) ^ ord(crib[3+k]) ^ ord(crib[4+k])
            if x == 0:
                print(i+j,crib[k:])
```

then i found that it showed 2 results for 31-33 range which looked promising. i xored them 2 at a time as well as parts of the flag to find the difference. i then asked willwam to find a solution but i also checked it with the solutions i generated. i then found `33 == 21 + 18` so the mid of 3 sections xored with flag part would get the other part of flag. this gave me "cap" as my 4th-6th characters. i used the chars i generated and bruteforced it and saw `"hata o sagashiteimQCE ka? dozo"`, `"tjctf{sE]Ymasen_flag_kudasaiYM"` which was using "isa". i brute forced the last char to get "isacapo" and

## "hata o sagashiteimasu ka? dozo, tjctf{sumimasen\_flag\_kudasaii}."

