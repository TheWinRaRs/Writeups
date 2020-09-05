# Alien Transmissions v2

## Brief

The aliens are at it again! We've discovered that their communications are in base 512 and have transcribed them in base 10. However, it seems like they used XOR encryption twice with two different keys! We do have some information:

* This alien language consists of words delimitated by the character represented as 481
* The two keys appear to be of length 21 and 19
* The value of each character in these keys does not exceed 255
* Find these two keys for me; concatenate their ASCII encodings and wrap it in the flag format.

481 is probably going to be the most common number, as this is the alien word delimiter. We can use this to execute a frequency attack.

The lowest common multiple of 21 and 19 is 399. The alien message was XORed with the 21 length key, and then the 19 length key. Because of how xor works, `message XOR first key XOR second key = message XOR (first key XOR second key)`

Therefore, if we stack the two keys against each other, and XOR \(that is 21  _19-length key XOR 19_  21-length key\) we get an "ultra-key" of length 399.

How can we derive this key? Frequency analysis, of course.

If we take every 399th number with different starting points\(like nums\[0::399\], nums\[1::399\], etc.\) then the subset of numbers we get from this will all be XORed with the same value!

This means we can get these subsets and run frequency analysis on them separately. The most common number is bound to be 481, so we can run freq analysis on these subsets, and the most common number will be 481 xored with the respective element of the "ultra-key". Using this, we can leak the ultra-key.

Now what? We've got 21  _19-length key XOR 19_  21-length key. Since ultimately this is to become a flag, courtesy of will, we can reduce the possible chars in each key to qwertyuiopasdfghjklzxcvbnmmQWERTYUIOPASDFGHJKLZXCVBNM1234567890\_,.'?!@$&lt;&gt;\*:-"

So...

We can generate a "mapping". By XORing every possible pair of chars in our alphabet, we can generate a mapping of possible values to the pair of characters that matches.

Then, we can significantly reduce the amount of possible chars we have for one key. We started with the 19-length key. Again, getting every 19th char starting at different starting points, we can get one char of the key XORed with lots of different other, PRINTABLE AND IN THE ALPHABET, values.

Essentially, for each character of the key, we can create a list of possible numbers such that every number is char xor K for some PRINTABLE AND IN THE ALPHABET K.

From there, we can use the alphabet as a whitelist for possible chars in one position of the key.

If it's impossible to xor a char and another char in the alphabet to get a certain number in the subset we create, then we know that char of the key can NOT be that.

Using a search like so,

```python
import string
import itertools
from Crypto.Util.strxor import strxor
def getfreqs(numbers):
    counts = {number: numbers.count(number) for number in set(numbers)}
    return counts
def getmax(freqs):
    return max(freqs.keys(), key=freqs.__getitem__)
def xor(b1,b2):
    return bytes(byte1 ^ byte2 for byte1,byte2 in zip(b1,b2))
with open("encrypted.txt") as f:
    lines = f.readlines()
    nums = [int(x) for x in lines]
common = 481
leakedkey = []
for i in range(399):
    subset = nums[i::399]
    freqs = getfreqs(subset)
    maximum = getmax(freqs)
    leak = maximum ^ common
    leakedkey.append(leak)
print(bytes(leakedkey))
mapping = {}
for pair in itertools.combinations_with_replacement("qwertyuiopasdfghjklzxcvbnmmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_,.'?!@$<>*:-",2):
    mapping[pair] = strxor(pair[0].encode(),pair[1].encode())[0]
print(mapping)
for i in range(21):
    subset = leakedkey[i::21]
    subset = list(filter(lambda x: x != 0,subset))
    possibles = list("qwertyuiopasdfghjklzxcvbnmmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_,.'?!@$<>*:-")
    for num in subset:
        for char in possibles:
            found = False
            for key in mapping:
                if mapping[key] == num:
                    if char in key:
                        found = True
            if not found:
                possibles.remove(char)
    print(possibles)
```

We can reduce the 19-length key to all of it's possible values in each position, getting:

```text
['X', '_']
['t', '*']
['h', 'm']
['3', '6']
['X', '_']
['5']
['3']
['f', 'c']
['0']
['k', 'n', '0']
['d', 'c']
['Z', '_']
['1', '6']
['2', '5', '*']
['X', '_']
['t']
['o', 'h', 'm']
['1', '6']
['2', '5']
```

we could use more frequency analysis to enumerate from there, but it's clear that this is going to be `_th3_53c0nd_15_th15`

From there, we simply XOR `_th3_53c0nd_15_th15` back with our ultra-key to get the first part of the flag, `h3r3'5_th3_f1r5t_h4lf`

### Flag: flag{h3r3'5\_th3\_f1r5t\_h4lf\_th3\_53c0nd\_15\_th15}

