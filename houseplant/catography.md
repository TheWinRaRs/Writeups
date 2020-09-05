# Catography

So pot got some json data which contained all of the image ids. I wrote a script that parsed this json, and used wget to grab the image files, and then read and parse the exifdata into a dictionary of `{image id: [latitude, longtitude]}` \(note certain parts of the below script are horrible written\)

Use day's coords and plot them with matplotlib \(code below\) then do some image manip

```python
import numpy as np
import matplotlib.pyplot as plt

def conversion(old):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    new = old.replace('deg',' ').replace('\'',' ').replace('"',' ')
    new = new.split()
    print(new)
    new_dir = new.pop()
    new.extend([0,0,0])
    print(new)
    return (int(new[0])+int(new[1])/60.0+float(new[2])/3600.0) * direction[new_dir]

with open("message.txt","r") as f:
    a = f.read()
    f.close()

ai = [i for i, x in enumerate(a) if x == "["]
aj = [i+1 for i, x in enumerate(a) if x == "]"]

print(len(ai)==len(aj))

print([a[ai[b]+1:aj[b]-1] for b in range(1)])
print([a[ai[b]:aj[b]] for b in range(1)])
c = [a[ai[b]+1:aj[b]-1].replace("\\","").split(",") for b in range(len(aj))]
print(conversion(c[0][1]))

plt.scatter([conversion(c[x][0]) for x in range(len(c))], [conversion(c[x][1]) for x in range(len(c))])
plt.show()
```

![flag](https://media.discordapp.net/attachments/699999846119243857/704012945780113488/flag.png)

## rtcp{4round\_7h3\_w0r1d}

