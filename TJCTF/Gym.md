# Gym

##### Download -> make executable -> create flag.txt

If we take a look at main, we can see that it basically says "starting weight is 211, try and get me down to 180 by day 7" 
(when we run the program, we're presented with 4 options to reduce weight. Have to do this in 7 days). If we rev main, we basically 
only care about this bottom bit
```python
user_input = input("What is your answer?")
iVar1 = int(user_input)

if iVar1 == 2:
    startweight -= 1
else:
    if iVar1 == 3:
        startweight -= 2
    else:
        if iVar1 != 4:
            counter += 1
    startweight -= 3
```
So here, we see that if we choose option 2, we subtract 1 from our weight. If our input isn't 2, then we go to the else. 
If input = 3, subtract 2. If not, then if our input is not 4, then increase the counter. 
But what we notice is that we always subtract 3 from our weight, if our answer wasn't 2.
So now for some simple maths:
```
211 - 180 = 31
31 = 6(2+3) - 1
```
Input in:
3
3
3
3
3
3
2
Wait 3 seconds, boom, profit

#### tjctf{w3iGht_l055_i5_d1ff1CuLt}
