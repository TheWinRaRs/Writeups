# Adventure

Similar to the original adventure, the flag is hidden in the easter egg thing of adventure

woa decided to diff the original and the given file, and found that 0xD80 to 0xDD0 changed

I went one step further and found an asm breakdown of the game [https://github.com/johnidm/asm-atari-2600/blob/master/adventure.asm](https://github.com/johnidm/asm-atari-2600/blob/master/adventure.asm)

Which shows the easter egg graphic being hidden here

The easter egg is hidden with the byte being converted to binary, and then being shown with a lit pixel as a 1 and an unlit as a 0

We can then take the differenced bytes and do the same to display the flag

I dont know what the flag is but uhhhhhhhh yeah i read it as

rgbCTF{b4c0n\_7nd\_3665}

Script below:

```python
a ="e0 80 80 01 07 e5 a7 60 e0 07 00 80 e7 a1 e3 01 07 60 80 87 84 67 05 07 e0 40 47 44 07 05 e7 80 c0 87 84 07 01 67 40 c0 46 62 03 02 86 e0 a0 e0 00 00 a0 a0 e0 20 20 00 00 e0 80 e0 00 00 e0 a0 a0 a0 e0 00 00 c0 a0 a0 00 00 e0 00 a0 a0 e0 20 20 00 00 c0 a0 a0 00 00 00 00 00 00 00 00 00 00"

a = a.split(" ")
for i in a:
  i = int(i,16)
  b = "{0:b}".format(i)
  c = ("0" * (8 -len(b))) + b
  d = c.replace("1","#")
  print(d.replace("0","-"))
```

## rgbCTF{b4c0n\_7nd\_3665}

