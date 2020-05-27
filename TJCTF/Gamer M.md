# Gamer M

After analysing the random.randint i found that it was rigged (info by botters) so i just reversed what it done (with help from tony) and pieced it together - code below  
#### tjctf{i5AJ0borFRenCx6342}

```python
def getindex(a):
    out = []
    for i in a:
        if "{" in i:
            out.append(0)
        if "3" in i:
            out.append(1)
        if "4" in i:
            out.append(2)
        if "2" in i:
            out.append(3)
        if "}" in i:
            out.append(4)
    return out

with open("out","r") as f:
    out = f.read()
    f.close()
out = out.split("\n")[:-2]
out = [[x[i:i+5] for i in range(0, len(x), 5)] for x in out ]
stats = ""
for j in range(5):
    for i in out:
        a = getindex(i)
        print(a)
        stats += str((a.index(j)-j)%5)
print(stats) # 4 is common
counter = [0,0,0,0,0]
for i in stats:
    counter[int(i)] += 1

print(counter)
for k in range(5):
    for j in range(5):
        alpha = out[0][getindex(out[0]).index(k)]
        alpha2 = {}
        for i in alpha:
            alpha2[i] = 0

        for i in out:
            thing = i[getindex(i).index(k)]
            thing = thing[-1]+thing[:-1] # revshift by 4
            alpha2[thing[j]] += 1

        for i in alpha:
            print(i,alpha2[i],end=" ")
        print()
```
