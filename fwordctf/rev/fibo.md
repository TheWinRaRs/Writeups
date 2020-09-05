# Fibo

Here's what the program does

First of all, use a mess function to encode the flag. This mess function is easily byte by byte bruteforceable if we use the printable range of characters.

Let's call this mflag.

```python
def mess(msg):
    enc=""
    for i in msg:
        enc+=chr((ord(i)+ord(i))%256)
    return enc
printable = string.printable
def demess(msg):
    # Byte by byte bruteforce
    dec = ""
    for i in range(len(msg)):
        for char in printable:
            if mess(char) == msg[i]:
                dec += char
                break
        else:
            dec += "-"
    return dec
```

Next, it pads the mflag so that it's length is a multiple of 9 using .

Then, it encrypts the mflag using matrix multiplication. Splitting the mflag into bunches of 9, it fills up a 3x3 matrix using the ascii values, multiplies it by a key that we know, transposes the resulting matrix, and turns it into a string result of of form

```text
matrix[0,0] matrix[0,1] matrix[0,2] matrix[1,0] .... ----- matrix2[0,0] .....
```

This is all done using the messig\_up function. Then, it takes the output, parses it, and uses an encode function to encode each of the numbers, writing them all to the output file. I didn't reverse the encode function, and instead just did a classic bruteforce to get the numbers which were all less than 2500.

Here's how the solve script operates.

1. Create a mapping of all possible encodings. Now, decode all the number encodings using this mapping.
2. Split the numbers into groups of 9, fill up 3x3 matrices, and transpose these matrices to get the pure matrix multiplication outputs.
3. Calculate the matrix inverse of the matrix key, then multiply the matrices by this inverse to get the original matrices
4. String together all these matrices back into a string by taking the ascii values\(we call round, as the results will be floats\) to get mess\(flag\)
5. Use our byte by byte bruteforce mess function to decode the messed flag.

Script below:

```python
import string
def mess(msg):
    enc=""
    for i in msg:
        enc+=chr((ord(i)+ord(i))%256)
    return enc
printable = string.printable
def demess(msg):
    # Byte by byte bruteforce
    dec = ""
    for i in range(len(msg)):
        for char in printable:
            if mess(char) == msg[i]:
                dec += char
                break
        else:
            dec += "-"
    return dec
import random
import numpy as np
key=np.matrix("1 2 3;0 1 4;5 6 0")
def recur_fibo(n):
    if n<=1:
        return 1
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
def messig_up(message,key):
    parts=""
    while len(message)!=0:
        to_work_with=message[:9]
        first_one=np.zeros((3,3))
        k=0
        for i in range(3):
            for j in range(3):
                first_one[i][j]=ord(to_work_with[k])
                k+=1
        finish=np.transpose(np.matmul(first_one,key))
        for i in range(3):
            for j in range(3):
                parts=parts + str(finish[i,j])+ " "
        parts+="-----"
        message=message[9:]
    return parts
def encode(n):
    i=1
    fib=recur_fibo(i)
    t_f=[]
    while fib<n:
        t_f.append(fib)
        i+=1
        fib=recur_fibo(i)
    _sum=0
    a_f=[]
    for i in range(len(t_f)-1,-1,-1):
        if _sum==n:
            break
        if _sum+t_f[i]<=n:
            a_f.append(t_f[i])
            _sum+=t_f[i]
    exis=[]
    for i in t_f:
        if i in a_f:
            exis.append(1)
        else:
            exis.append(0)
    return t_f,exis
encmap = []
for i in range(2500):
    encmap.append(encode(i))
stuff = open("output.txt").readlines()
data = []
for line in stuff:
    data.append(eval(line))
nums = []
for piece in data:
    nums.append(encmap.index(piece))
print(nums)
invkey = np.linalg.inv(key)
dec = ""
for i in range(0,len(nums),9):
    split = nums[i:i+9]
    goodmat = np.array([split[j:j+3] for j in range(0,9,3)])
    goodmat = np.transpose(goodmat)
    matr = np.matmul(goodmat,invkey)
    print(matr)
    for x in range(3):
        for y in range(3):
            dec += chr(round(matr[x,y]))
print(len(dec))
print(demess(dec).encode())
```

## Flag: FwordCTF{whatever\_you\_do\_i\_can\_do\_it\_better!!!!}

