# snakes everywhere

This was actually readable byte code. 

Had trouble understanding for loops but now it makes sense. 

In general this is what it actually was. 

I just undid the operations and got flag (had trouble with nums out of range but fixed with %256.
```python
ef crypt():
    for i in range(len(flag)//3):
        ct += chr(ord(key[i])*ord(flag[i])-i)

    for i in range(len(flag)//3,len(flag)//3*2):
        ct += chr(ord(flag[i])*ord(key[i%len(key)])+i)

    for i in range(len(key)//2,len(flag)):
        ct += key[i%16]^flag[i]
 ```
 
 #### zh3r0{Python_disass3mbly_is v3ry_E4sy}
