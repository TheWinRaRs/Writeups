# AP Lab: English Language

Let's look at the source code. It gets an input, and checks if it's length is 23 first of all. If not, it automatically tells you your input is wrong.

Then, it goes in a for loop. This loop will iterate 3 times. Each time, it sets inp(variable containing the input) to transpose(inp), and then to xor(inp)

Essentially, 3 times, it transposes then xors the input.

the xor is self explanatory, it xors the input with a key.

The transposing is a little different. It has a list of numbers, then does the equivalent of this in java(if the list of numbers was called nums)

return ''.join(inp[i] for i in nums)

We can reverse this relatively simply with a python script, and get the flag.
```python
key = [4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]
indexes =  [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
enc =  b"1dd3|y_3tttb5g`q]^dhn3j"
def detranspose(transposed):
    dicto = dict(zip(indexes,transposed))
    ans = []
    for i in range(23):
        ans.append(dicto[i])
    return bytes(ans)
def solve(encrypted):
    stage1 = bytes(b1 ^ b2 for b1,b2 in zip(encrypted,key))
    return detranspose(stage1)
cur = enc
for _ in range(3):
    cur = solve(cur)
print(cur)
```
