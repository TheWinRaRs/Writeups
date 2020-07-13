# rubikcbc

im aware there is a module for this but:
1. idk how to use it
2. i dont want my effort to go to waste (since i made my own cube manipulator)
3. i dont like installing one time modules cus they clog up space

since it was just cbc i just had to map it to a cube and reverse the scramble
then xorred it to get a pdf file

i spent too long fixing bugs with the xor process and how bytes are handled
i also spent too long fixing bugs of my cube program

found a qr code in pdf and...

Script:
```python

'''
so uhhh orange top green front

   OOO
   OOO
   OOO
YYYWWWGGGBBB - form LRFB
YYYWWWGGGBBB
YYYWWWGGGBBB
   RRR
   RRR
   RRR

   OOO
   OOO
   YYY
YYRWWWOGGBBB
YYRWWWOGGBBB
YYRWWWOGGBBB
   GGG
   RRR
   RRR

   WWW
   WWW
   WWW
RRRRRGOOOYYY
YYYRRGGGGOOO
YYYRRGGGGOOO

BYY
YWY
ORG

RRGYBBYOOGGGRROBBBWOOGGGRGWOOOBBBRRWWYWWYWRWY
'''

facestring = "WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY"

def format(a):
    out = ""
    a = a.replace("'","22")
    for i in a.split(" "):
        out += (i[0] + " ")*len(i)
    out = out[:-1]
    return out


def nice(a):
    for i in range(3):
        print("   "+a[i*3:i*3+3])
    for i in range(3):
        print(a[i*12+9:i*12+21])
    for i in range(3):
        print("   "+a[i*3+45:i*3+48])

def strface(a):
    new = [[["" for _ in range(3)] for _ in range(3)] for _ in range(6)]
    for i,j in enumerate(a[:9]):
        new[0][i//3][i%3] = j
    for i,j in enumerate(a[-9:]):
        new[5][i//3][i%3] = j
    mid = a[9:-9]
    for i in range(36):
        new[(i//3)%4+1][i//12][i%3] = mid[i]
    return new

def facestr(a):
    new = ""
    for i in a[0]:
        new += "".join(i)
    for i in range(3):
        for j in a[1:-1]:
            new += "".join(j[i])
    for i in a[-1]:
        new += "".join(i)
    return new

def bfacestr(a):
    new = []
    for i in a[0]:
        new += i
    for i in range(3):
        for j in a[1:-1]:
            new += j[i]
    for i in a[-1]:
        new += i
    return new

print(strface(facestring))
print(facestr(strface(facestring)))

def r(face , n = 1):
    for i in range(n):
        face = [list(x) for x in zip(*face[::-1])]
    return face

def shift(faces, nums):
    new = [x[:] for x in faces]
    newnums = nums[-1:] + nums[:-1]
    for i in range(4):
        new[newnums[i]][0] = faces[nums[i]][0]
    return new

def spin(faces,a):
    if a == 0:
        return faces
    if a == 1:
        return [r(faces[1]),r(faces[5]),r(faces[2]),r(faces[0]),r(faces[4],3),r(faces[3])]
    if a == 2:
        return [faces[2],r(faces[1],3),faces[5],r(faces[3]),r(faces[0],2),r(faces[4],2)]
    if a == 3:
        for i in range(3):
            faces = spin(faces,1)
        return faces
    if a == 4:
        for i in range(3):
            faces = spin(faces,2)
        return faces
    if a == 5:
        for i in range(2):
            faces = spin(faces,2)
        return faces

def turn(faces,a):
    b = ["U","L","F","R","B","D"].index(a)
    new_faces = spin(faces,b)

    new_faces[0] = r(new_faces[0])
    new_faces = shift(new_faces,[1,2,3,4])


    for i in range(3):
            new_faces = spin(new_faces,b)

    return new_faces

turns = "F' D F L' F U R' B2 U' D' L U2 D F2 L2 B2 L2 D"
turns = format(turns)
print(turns)
IV = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuv"

with open("enc_","rb") as f:
    kek = f.read()
    f.close()

kek2 = [kek[i*54:i*54+54] for i in range(len(kek)//54)]

out = b""

for kek3 in kek2:
    cube = strface(kek3)
    for i in turns.split(" "):
        cube = turn(cube,i)

    pp1 = bfacestr(cube)
    pp2 = bytes([_a ^ _b for _a, _b in zip(pp1, IV)])
    out += pp2

    IV = kek3

#print(out)

with open("out","wb") as f:
    f.write(out)
    f.close()
```

#### rgbCTF{!IP_over_Avian_Carriers_with_QoS!}
