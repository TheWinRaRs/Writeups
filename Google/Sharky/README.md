# Sharky - Crypto

This challenge involved reversing the sha256 hash function where there were unknown keys.

## Intro

Unlike some of my other writeups where I reverse everything there is in a pretty logical order, I want to walk through how I personally solved the challenge, since I did it in a rather strange order.

## Reversing challenge.py

I obviously had to start by taking a look at the challenge.py file first, since it had the main functions and what was happening.

We see that challenge.py
- starts by calling the generate_random_round_keys with parameter of 8
- calls the sha256_with_secret_round_keys with the round keys and our message, which if we look is 'Encoded with random keys', and is constant
- prints the hex result of sha256_with_secret_round_keys
- prompts the user to enter a number of keys in hex, seperated with a comma
  - and makes sure the number of keys entered is 8
- compares the keys entered by the user to the actual secret keys used n the sha256_with_secret_round_keys function
  - if they all match, then it prints `Good job, here's a flag: `, along with the flag
  - if not, then it prints `Sorry, that's not right.`

So, we need to deduce the keys used in the sha256 function when we know the message and the hash created by that message with the keys.

If we take a look at the generate_random_round_keys function, we see it just generates a 32 bit number n times, where n is the number passed to the function, more specifically, it generates a number between 0 and 256 4 times and concatenates the numbers together.
Nothing vulnerable here.

```python
def generate_random_round_keys(cnt: int):
  res = {}
  for i in range(cnt):
    rk = 0
    for b in os.urandom(4):
      rk = rk * 256 + b
    res[i] = rk
  return res
```

Then, we look at the sha256_with_secret_round_keys function.

```python
  sha = sha256.SHA256()
  round_keys = sha.k[:]
  for i, v in secret_round_keys.items():
    round_keys[i] = v
  return sha.sha256(m, round_keys)
```

We see that it just calls the sha.sha256 function on the message, along with the round keys that were generated.

It seems that the sha.sha256 is imported and given to us in the sha256.py file, so we need to go have a look at that.

## The sha256.py file

This file seems to be the actual crypto part of the challenge.

Taking a quick look at the program, I deduced that it performs 64 rounds of the compression function on our padded message.

Since we know the message and it stays constant, we can use the given compute_w function to generate the w for our message.

We also know the k values, so we can just use those.

## Reversing a round with all values

My first goal was to try and figure out how to reverse a round of one of these functions.

We can take a closer look at the compression function, and see that

```python
  def compression_step(self, state, k_i, w_i):
    a, b, c, d, e, f, g, h = state
    s1 = self.rotate_right(e, 6) ^ self.rotate_right(e, 11) ^ self.rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    tmp1 = (h + s1 + ch + k_i + w_i) & 0xffffffff
    s0 = self.rotate_right(a, 2) ^ self.rotate_right(a, 13) ^ self.rotate_right(a, 22)
    maj = (a & b) ^ (a & c) ^ (b & c)
    tmp2 = (tmp1 + s0 + maj) & 0xffffffff
    tmp3 = (d + tmp1) & 0xffffffff
    return (tmp2, a, b, c, tmp3, e, f, g)
```
only 2 values actually change, which are d and h, the rest are just shifted right by 1 place. 

We also see that, because of this, we can calculate quite a few variables mentioned, 4 to be exact, which are s1, ch, maj and s0, using the given functions.

Now, we need to figure out what d and h are, from tmp2 and tmp3.

We know that:

tmp1 = h + s1 + ch + k_i + w_i
tmp2 = tmp1 + s0 + maj
tmp3 = d + tmp1

Each of these are then taken mod 4294967296 (referring this to p from now on).

Rewriting these, we get 
tmp1 = h + s1 + ch + k_i + w_i
tmp2 = h + s1 + ch + k_i + w_i + s0 + maj
tmp3 = h + s1 + ch + k_i + w_i + d 

Now, we know tmp2 and tmp3, so we and in the case of tmp2, we can just subtract all our known values and take that mod p to get h

Then, since we know h, we can then carry on to work out d, subtracting all the values from tmp3 and taking that mod p to get d.

So now we know how to reverse a round in the case where we know all the previous values, and also the k_i and w_i values.

I wrote a messy function in python to do this:

```python
def getprev(state,k_i,w_i):
  tmp2, a, b, c, tmp3, e, f, g = state
  s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
  ch = (e & f) ^ (~e & g)
  s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
  maj = (a & b) ^ (a & c) ^ (b & c)
  tmp1 = (tmp2 - (s0 + maj)) % p
  bleh = s1 + ch + k_i + w_i
  h = (tmp1 - bleh) % p
  d = (tmp3 - tmp1) % p
  return [a,b,c,d,e,f,g,h]
```

Now, once I had this done, I thought I had solved the challenge, and that the goal was to recover the initial state of the hash function, since there were 8 keys, and so I was suprised when it didn't work.


## Not over yet :/

Taking another look at the script however, we can see that the keys generated are used as the first 8 k values, however the rest remain unchanged, and the state is constant.

Knowing this, if we know the initial state and the fact that values each round are shifted right by one, we generate this table: (using sample values here)

[1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924,  528734635, 1541459225] # initial state (pre-rounds)

[xxxxxxxxxx, 1779033703, 3144134277, 1013904242, xxxxxxxxxx, 1359893119, 2600822924,  528734635]

[xxxxxxxxxx, xxxxxxxxxx, 1779033703, 3144134277, xxxxxxxxxx, xxxxxxxxxx, 1359893119, 2600822924]

[xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, 1779033703, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, 1359893119]

[2788502447, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx]

[ 523352746, 2788502447, xxxxxxxxxx, xxxxxxxxxx, 1827710523, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx]

[ 155539695,  523352746, 2788502447, xxxxxxxxxx,  277694853, 1827710523, xxxxxxxxxx, xxxxxxxxxx]

[3585474043,  155539695,  523352746, 2788502447, 4184759956,  277694853, 1827710523, xxxxxxxxxx]

[4286495597, 3585474043,  155539695,  523352746, 3141120170, 4184759956,  277694853, 1827710523] # 7th state

Now, at the time I didn't realise this, but my getprev function was able to recover the entirety of the first half of the table, since I believe that the first half
of the values aren't affected by the second half, while the second half are.

So, now we know the entirety of the first 4 columns of the table.

However, there are still 4 32 bit numbers which we don't know.

[1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924,  528734635, 1541459225] # inital state

[1348132138, 1779033703, 3144134277, 1013904242, xxxxxxxxxx, 1359893119, 2600822924,  528734635]

[2733599647, 1348132138, 1779033703, 3144134277, xxxxxxxxxx, xxxxxxxxxx, 1359893119, 2600822924]

[1127758716, 2733599647, 1348132138, 1779033703, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, 1359893119]

[2788502447, 1127758716, 2733599647, 1348132138, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx]

[ 523352746, 2788502447, 1127758716, 2733599647, 1827710523, xxxxxxxxxx, xxxxxxxxxx, xxxxxxxxxx]

[ 155539695,  523352746, 2788502447, 1127758716,  277694853, 1827710523, xxxxxxxxxx, xxxxxxxxxx]

[3585474043,  155539695,  523352746, 2788502447, 4184759956,  277694853, 1827710523, xxxxxxxxxx]

[4286495597, 3585474043,  155539695,  523352746, 3141120170, 4184759956,  277694853, 1827710523] # our 7th state

Since we know the initial state, we should probably only look at the initial state and the one after it, since we have more values, 
and if we are able to work out the 5th value in that second row, it basically becomes the exact same problem on each row.

```python
  def compression_step(self, state, k_i, w_i):
    a, b, c, d, e, f, g, h = state
    s1 = self.rotate_right(e, 6) ^ self.rotate_right(e, 11) ^ self.rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    tmp1 = (h + s1 + ch + k_i + w_i) & 0xffffffff
    s0 = self.rotate_right(a, 2) ^ self.rotate_right(a, 13) ^ self.rotate_right(a, 22)
    maj = (a & b) ^ (a & c) ^ (b & c)
    tmp2 = (tmp1 + s0 + maj) & 0xffffffff
    tmp3 = (d + tmp1) & 0xffffffff
    return (tmp2, a, b, c, tmp3, e, f, g)
```

The important thing to notice here is that the only place where k_i is used at all is when calculating tmp1, and so we can calculate all the other values except tmp1 (and therefore tmp2 and tmp3).

We can then get our equations from before:

tmp1 = h + s1 + ch + k_i + w_i
tmp2 = h + s1 + ch + k_i + w_i + s0 + maj
tmp3 = h + s1 + ch + k_i + w_i + d 

Since we know everything for tmp1 except for k_1, I'm going to write a new equation: 

temp = h + s1 + ch + w_i

Then we can rewrite the equations:

tmp1 = temp + k_i
tmp2 = temp + k_i + s0 + maj
tmp3 = temp + k_i + d

Now, we can work out what our new variable temp is, since all the values we have, and then we can also easily calculate k_i since we know tmp2, and so we just 
subtract (temp + s0 + maj) from tmp2 to get k_i, which we then use to calculate tmp3!

We then fill in our table in the four cells where tmp3 is used, and then repeat for the next row, since we know all values again (apart from k_i of course!)

Again, another messy python function to solve:

```python
def remove(matrix): 
  matrix[1][1] = 1779033703
  matrix[2][2] = 1779033703
  matrix[3][3] = 1779033703
  matrix[1][2] = 3144134277
  matrix[2][3] = 3144134277
  matrix[1][3] = 1013904242
  matrix[1][5] = 1359893119
  matrix[2][6] = 1359893119
  matrix[3][7] = 1359893119
  matrix[1][6] = 2600822924
  matrix[2][7] = 2600822924
  matrix[1][7] = 528734635
  return matrix

def solvepart2(matrix): 
  matrix = remove(matrix)
  for i in range(4):
    w_i = w[i+i]
    a, b, c, d, e, f, g, h = matrix[i]
    tmp2 = matrix[i+1][0]
    s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
    maj = (a & b) ^ (a & c) ^ (b & c)
    temp = s1 + ch + w_i
    temp2 = s0 + maj
    hki = (tmp2 - temp2) % p
    tmp3 = (d + hki) % p
    matrix[i+1][4] = tmp3
    matrix[i+2][5] = tmp3
    matrix[i+3][6] = tmp3
    matrix[i+4][7] = tmp3
  return matrix
```

Once we have our solution matrix, I made another function just to get the k_i values and output them.

```python
def getkeys(sol):
  keys = []
  for i in range(8):
    a, b, c, d, e, f, g, h = sol[i]
    w_i = w[i]
    s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    thing = w_i + ch + s1 + d + h 
    value = sol[i+1][4]
    key = (value - thing) % p
    keys.append(key)
  keys = [str(hex(x))[2:] for x in keys ]
  return keys
```

## Final tweaks

After all the rounds, we see a line in the sha256 function before the state gets returned to the player:
```python
state = [(x + y) & 0xffffffff for x, y in zip(state, s)]
```

This basically
- takes x from the current state and y from the initial state
- adds them together
- takes it mod p

This is once again very easy to reverse, we just take our outputted hash, subtract each number of the initial state from it, and then mod p once again.

Now we have all the steps done, we just need to put it all together.

Final solve script:

```python

import struct

# rotate right function provided by server
def rotate_right(v, n):
  w = (v >> n) | (v << (32 - n))
  return w & 0xffffffff

# setting values to their actual value instead of our fake value
def remove(matrix): 
  matrix[1][1] = 1779033703
  matrix[2][2] = 1779033703
  matrix[3][3] = 1779033703
  matrix[1][2] = 3144134277
  matrix[2][3] = 3144134277
  matrix[1][3] = 1013904242
  matrix[1][5] = 1359893119
  matrix[2][6] = 1359893119
  matrix[3][7] = 1359893119
  matrix[1][6] = 2600822924
  matrix[2][7] = 2600822924
  matrix[1][7] = 528734635
  return matrix

## compute w for our particular message

# make sure its padded
def padding(m):
  lm = len(m)
  lpad = struct.pack('>Q', 8 * lm)
  lenz = -(lm + 9) % 64
  return m + bytes([0x80]) + bytes(lenz) + lpad

# get our w
def compute_w(m):
  m = padding(m)
  w = list(struct.unpack('>16L', m))
  for _ in range(16, 64):
    a, b = w[-15], w[-2]
    s0 = rotate_right(a, 7) ^ rotate_right(a, 18) ^ (a >> 3)
    s1 = rotate_right(b, 17) ^ rotate_right(b, 19) ^ (b >> 10)
    s = (w[-16] + w[-7] + s0 + s1) & 0xffffffff
    w.append(s)
  return w

## constant values
start = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225]
k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
w = compute_w(b'Encoded with random keys')

## convert the hash into the last state of the message
def hash2nums(hashed):
  state = []
  x  = [hashed[i:i+8] for i in range(0, len(hashed), 8)]
  for i in range(len(x)):
    j = x[i]
    j = int(j,16)
    j -= start[i]
    state.append(j%p)
  return state

## reversing the round when we have all info
def getprev(state,k_i,w_i):
  tmp2, a, b, c, tmp3, e, f, g = state
  s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
  ch = (e & f) ^ (~e & g)
  s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
  maj = (a & b) ^ (a & c) ^ (b & c)
  tmp1 = (tmp2 - (s0 + maj)) % p
  bleh = s1 + ch + k_i + w_i
  h = (tmp1 - bleh) % p
  d = (tmp3 - tmp1) % p
  return [a,b,c,d,e,f,g,h]

## get to the 7th state so we can grab our keys
def get27thstate(state):
  states = []
  for i in range(63,0,-1):
    k_i = k[i]
    w_i = w[i]
    state = getprev(state,k_i,w_i)
    if i <= 8:
      states.append(state)
  states.append(start)
  return states

## when we get to round 7, we need to do other stuff, since we dont have all values
def solvepart2(matrix): 
  ## remove all weird values
  matrix = remove(matrix)
  for i in range(4):
    w_i = w[i+i]
    a, b, c, d, e, f, g, h = matrix[i]
    tmp2 = matrix[i+1][0]
    s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
    maj = (a & b) ^ (a & c) ^ (b & c)
    temp = s1 + ch + w_i
    temp2 = s0 + maj
    hki = (tmp2 - temp2) % p
    tmp3 = (d + hki) % p
    matrix[i+1][4] = tmp3
    matrix[i+2][5] = tmp3
    matrix[i+3][6] = tmp3
    matrix[i+4][7] = tmp3
  return matrix


## working out the key values to submit to the server
def getkeys(sol):
  keys = []
  for i in range(8):
    a, b, c, d, e, f, g, h = sol[i]
    w_i = w[i]
    s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
    ch = (e & f) ^ (~e & g)
    thing = w_i + ch + s1 + d + h 
    value = sol[i+1][4]
    key = (value - thing) % p
    keys.append(key)
  keys = [str(hex(x))[2:] for x in keys ]
  return keys

## final solve function
def solve(hashed):
  state = hash2nums(hashed)
  states = get27thstate(state)
  sol = solvepart2(states[::-1])
  keys = getkeys(sol)
  print(f'Solution: {",".join(keys)}')

p = 4294967296 # we'll take everything mod this to get rid of the & with p-1
hash = "93dc2d9e92adc268ba4fcda976920d286389bd047de5c15f924e8cd1216a4666"
solve(hash)
```

Flag: CTF{sHa_roUnD_k3Ys_caN_b3_r3vERseD}
