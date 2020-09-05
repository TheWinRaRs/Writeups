# Post-Homework Death

I thought it was just a normal matrix calc but that was wrong since it had a weird way of formatting it made a script tho

```python
def matrix():
    dec = [
    [1.6,  -1.4,  1.8],
    [2.2,  -1.8,  1.6],
    [-1 ,    1 ,   -1]]
    out = []
    pp = 0
    string = [37,36,-1,34,27,-7,160,237,56,58,110,44,66,93,22,143,210,49,11,33,22]
    for i in range(int(len(string)/3)):
        a = string[i*3:i*3+3]
        for j in range(3):
            pp = 0
            for k,l in enumerate(a):
                pp += l*dec[j][k]
            out.append(int(pp))
    for i in out:
        print(chr(i+96),end="")
```

## rtcp{go\_do\_your\_homework}

