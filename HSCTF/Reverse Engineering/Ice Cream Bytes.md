# Ice Cream Bytes

There's a text file IceCreamManual.txt. It's actual contents aren't important, more what happens to it. The program reads all bytes from this file, then calls fillMachine on it. fillMachine basically grabs specific indexes of the file and puts them together into a byte string. I recreated this function in python and ran it to get the string lollookatthistextigotfromthemanual. The code calls 4 functions on our input, then compares the final result to that string. So we must reverse from that string back to the flag.

The 4 functions it calls, in order, are strawberry shuffle -> vanilla shuffle -> chocolate shuffle -> toppings

We'll work in reverse, going back one step each time to get the original input.

First things first: toppings.
Toppings basically takes an array of bytes(bytes can be negative in java! It's weird, but largely unimportant) and every byte of the output is the respective byte of the input + the respective byte of the toppings byte array. We can simply subtract the values.

Next: chocolate shuffle

This code is a bit more complicated. For every index in the output:
if an even index, AND index is > 0, set output[i] = input[i - 2]
if an even index, and index IS 0, set output[i] = input[33]

if an odd index, AND index is < 32, output[i] = input[i + 2]
if an odd index, and index >= 32, output[i] = input[1]

We can basically recreate the loop in python and swap around the indexes, e.g

input[i + 2] = output[i]

to reverse this step.

Next: vanilla shuffle.

This is simple. For every index in the input - if the index is even, add 1 to the byte value. If the index is odd, subtract 1. Again, easily reversible with a simple loop.

Finally, strawberry shuffle. The final thing to reverse to get the flag. The code looks a bit weird at first, but in reality all it does is reverse the string.

If we string all these things together, we get the flag. Script below.
```python
def fillmachine(inputIceCream):
    output = [0 for _ in range(34)]
    intGredients = [27, 120, 79, 80, 147, 
            154, 97, 8, 13, 46, 31, 54, 15, 112, 3, 
            464, 116, 58, 87, 120, 139, 75, 6, 182, 
            9, 153, 53, 7, 42, 23, 24, 159, 41, 110]
    for i in range(34):
        output[i] = inputIceCream[intGredients[i]]
    return bytes(output)
def reversetoppings(inputcream):
    output = [0 for _ in range(34)]
    toppings = [4, 61, -8, -7, 58, 55, 
            -8, 49, 20, 65, -7, 54, -8, 66, -9, 69, 
            20, -9, -12, -4, 20, 5, 62, 3, -13, 66, 
            8, 3, 56, 47, -5, 13, 1, -7]
    for index,element in enumerate(inputcream):
        output[index] = element - toppings[index]
    return bytes(output)
def revchoco(inputcream):
    output = [1 for _ in range(34)]
    for i in range(34):
        if i % 2 == 0:
            if i > 0:
                output[i - 2] = inputcream[i]
            else:
                output[33] = inputcream[i]
        else:
            if i < 32:
                output[i + 2] = inputcream[i]
            else:
                output[1] = inputcream[i]
    return bytes(output)
def revvanilla(inputcream):
    output = [0 for _ in range(34)]
    for i in range(34):
        if i % 2 == 0:
            output[i] = inputcream[i] - 1
        else:
            output[i] = inputcream[i] + 1
    return bytes(output)
def revberry(inputcream):
    output = [0 for _ in range(34)]
    for i in range(34):
        output[34 - i - 1] = inputcream[i]
    return bytes(output)
target = fillmachine(open("manual.txt", "rb").read())
print(target)
stage1 = reversetoppings(target)
print(stage1)
stage2 = revchoco(stage1)
print(stage2)
stage3 = revvanilla(stage2)
print(stage3)
flag = revberry(stage3)
print(flag)
```
