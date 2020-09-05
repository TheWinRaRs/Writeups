# Dozen Bases

From listening to the audio, I realised that it was DTMF tones immediately. \(The website I usually use: [http://www.dialabc.com/sound/detect/index.html](http://www.dialabc.com/sound/detect/index.html) was broken, so I had to do it another way, using a weird tool or somethin and then manually correct stuff with audacity, but lets pretend it worked to make things simple\) Once we decoded the tones, we got a string of characters, which was 'A288439640A3A140997B8A9945987B8844838B85847B419298407B447B978186437B99454192877B5870655AA5' From the title, we can guess that this is base12, and since there was a gap between each 2 tones, I guessed that it was just each 2 tones was the base12 of a character. I wrote a short python script to convert it to the flag.

```python
line = "A288439640A3A140997B8A9945987B8844838B85847B419298407B447B978186437B99454192877B5870655AA5"
print(len(line))
n = 2
x  = [line[i:i+n] for i in range(0, len(line), n)]
o = ""
for i in x:
  o += chr(int(i,12))
  b.append(chr(int(i,12)))
print(o)
```

## Flag: zh3r0{y0u\_ju5t\_h4cked\_1nt0\_4\_saf3\_u51ng\_DTMF}

