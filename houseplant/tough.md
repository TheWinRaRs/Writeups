# Tough

First I made a python script

```python
"""i made a rev createmap func"""
def antimap(owo,uwu):
    inputs = ""
    realflag = [9,4,23,8,17,1,18,0,13,7,2,20,16,10,22,12,19,6,15,21,3,14,5,11]
    therealflag = [20,16,12,9,6,15,21,3,18,0,13,7,1,4,23,8,17,2,10,22,19,11,14,5]
    if uwu:
        for i in range(len(realflag)):
            inputs += owo[realflag[i]]
    else:
        for i in range(len(realflag)):
            inputs += owo[therealflag[i]]
    print(inputs)
    return inputs
"""and then figured i could skip the last stage and deal with it later so i rev the third stage"""
def rev():
    zz = [157, 157, 236, 168, 160, 162, 171, 162, 165, 199, 169, 169, 160, 194, 235, 207, 227, 210, 157, 203, 227, 104, 212, 202]
    finals = []
    createMap(theflags0, flag, False)#44ytc3whr_040_rhw___o4uk

    for i in range(len(zz)):
        print(theflags0[i],end="")
        finals.append(zz[i]-ord(theflags0[i]))
    print(finals)
```

This gives `"iis4=o4:3hyupcygls>lt4__"` and i put it into my revmap func seperately since it's also seperate when making the flag.

```text
iis4=o4:3hyupcygls>lt--- => h=-3si>ic:stly-pl4g-4you
---------------------4__ => ------4-------_----_----
```

and combined them to get `h=-3si4ic:stly_pl4g_4you` but i also mapped which chars could've been affected by 4th stage `nm-mnmnmnmnnnnnmnnnnnnmn` - where n is no and m is maybe affected `h=-3si>ic:stly-pl4g-4you` - i tested around and got...

## rtcp{h3r3s\_4\_c0stly\_fl4g\_4you}

