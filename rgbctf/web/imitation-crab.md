# imitation crab

robots.txt gives a `har` file link where we can see a log file after mashing keyboard i saw that the post request contained a "char" parameter so i extracted all of those from the har file and then converted those values to ascii to get flag

script below:

```python
o = ""
with open("export.har","r") as f:
  for line in f:
    if '"text": "{' in line:
      o += chr(int(line[31:33]))
print(o)
```

## RGBCTF{H4R\_F1L3S\_4R3\_2UP3R\_US3FU1}

