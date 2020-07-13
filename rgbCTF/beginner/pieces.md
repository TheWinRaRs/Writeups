# Pieces

Each character is divided by two, if it evenly divides `|` is used, else `/`.

I just had to multiply each ascii value by two, then add 1 accordingly.
```python
inp = "9|2/9/:|4/7|8|4/2/1/2/9/"
for i in range(0, len(inp), 2):
    char = ord(inp[i])
    mod = inp[i+1]
    char = char*2
    if mod == '/':
        char+=1
    print(chr(char), end='')
```
#### rgbCTF{restinpieces}
