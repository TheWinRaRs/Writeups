# 12 Shades of Redpwn

Starting from the top as 0, 
represent each colour as a base12 digit to get `86908187A349994397974192497B41977B44927B449698A5`.

Then convert from base12 each 2 chars to get flag:
```python
line = "86908187A349994397974192497B41977B44927B449698A5"
n = 2
x  = [line[i:i+n] for i in range(0, len(line), n)]
o = ""
for i in x:
  o += chr(int(i,12))
print(o)
```

#### flag: flag{9u3ss1n9_1s_4n_4rt}
