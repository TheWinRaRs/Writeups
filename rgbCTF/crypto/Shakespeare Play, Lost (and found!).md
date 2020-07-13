# Shakespeare Play, Lost (and found!)

Each line has two numbers. I guessed that the numbers were encoding

line of play, character of line

So, just write a script to parse the data, then grab the appropriate lines and characters, then concatenate to get the flag.

```python
play = """A long lost play about trees, written exclusively by Shakespeare for RGBSec.

Romeo, apparently a rapidly changing multicolored tree.
Hamlet, a person who can't make up his mind.


                    Act I: Colorful Tree.

                    Scene I: Fast-changing Tree.

[Enter Hamlet and Romeo]

Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a red green blue red green tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a red tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green blue tree! You are as lovely as the sum of a  tree and thyself! Speak your mind!
Hamlet: You are nothing! You are a red green blue red green tree! You are as lovely as the sum of a red green blue red tree and thyself! You are as lovely as the sum of a red green blue tree and thyself! You are as lovely as the sum of a  tree and thyself! Speak your mind!
[Exeunt]
"""
nums = """33, 20
71, 5
43, 142
60, 150
73, 312
78, 66
15, 22
12, 115
29, 18
51, 147
45, 68
34, 14
54, 126
15, 48
3, 4
60, 126
45, 77
13, 69"""
nums = nums.split('\n')
nums = [[int(x) for x in y.split(', ')] for y in nums]
play = play.split('\n')
flag = ''
for pair in nums:
    flag += play[pair[0]][pair[1]]
print(flag)
```

#### Flag: rgbCTF{itsanrgbtreeeeeee!}
