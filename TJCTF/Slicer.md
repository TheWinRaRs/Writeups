# Slicer

If we open this up in a gcode editor, we can see a fake flag there.
The hint hints at the movement speed of the arm, and so if we do a bit of research into this, 
we can see they are represented by "F" values. Therefore, we extract these from the gcode file.
Most of them are either `F10500` or `F2400`, but some of them appear to be quite small,
and some even appear to be within the range of numbers for standard ASCII chars. 
Perhaps there is something hidden in those values...  
So, we filter out the `F10500` and `F2400` values.  
At the end of the output, we can see a list of values that appear to be within the ASCII number range, 
so I converted these numbers to ASCII text to get the flag.  
```
F116
F106
F99
F116
F102
F123
F109
F52
F110
F121
F95
F108
F52
F121
F51
F114
F115
F125
```
#### Flag: tjctf{m4ny_l4y3rs}
