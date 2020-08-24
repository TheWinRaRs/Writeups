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