# Flag-SP network

2 byte key, we can feasibly bruteforce. All that's left to do is write a decrypt function.

#### Flag: flag{i_guess_2_bytes_wasnt_enough_after_all}
```py
import random

rounds = 5
block_size = 8

invsa = {
  0: 1,
  1: 13,
  2: 14,
  3: 9,
  4: 3,
  5: 6,
  6: 5,
  7: 4,
  8: 8,
  9: 10,
  10: 7,
  11: 2,
  12: 12,
  13: 0,
  14: 15,
  15: 11
}

invsb = {
  0: 3,
  1: 11,
  2: 4,
  3: 10,
  4: 9,
  5: 1,
  6: 2,
  7: 8,
  8: 13,
  9: 0,
  10: 6,
  11: 7,
  12: 15,
  13: 12,
  14: 5,
  15: 14
}
key = [47, 16, 47, 16, 47, 16, 47, 16]


to_bin = lambda x, n=block_size: format(x, "b").zfill(n)
to_int = lambda x: int(x, 2)
to_chr = lambda x: "".join([chr(i) for i in x])
to_ord = lambda x: [ord(i) for i in x]
bin_join = lambda x, n=int(block_size / 2): (str(x[0]).zfill(n) + str(x[1]).zfill(n))
bin_split = lambda x: (x[0 : int(block_size / 2)], x[int(block_size / 2) :])
str_split = lambda x: [x[i : i + block_size] for i in range(0, len(x), block_size)]
xor = lambda x, y: x ^ y

def sinv(a, b):
    return invsa[a], invsb[b]

def pinv(a):
    return a[2] + a[5] + a[0] + a[5] + a[1] + a[7] + a[6] + a[4]

def ks(k):
    return [
        k[i : i + int(block_size)] + k[0 : (i + block_size) - len(k)]
        for i in range(rounds)
    ]


def kx(state, k):
    return [xor(state[i], k[i]) for i in range(len(state))]


def eee(i):
  a, b = bin_split(to_bin(ord(i)))
  sa, sb = s(to_int(a), to_int(b))
  pe = p(
            bin_join((to_bin(sa, int(block_size / 2)), to_bin(sb, int(block_size / 2))))
        )
  return to_int(pe)

def dec(ct):
  decrypted = []
  for i in ct:
    for pt in range(256):
      if eee(chr(pt)) == ord(i):
        decrypted.append(pt)
  return decrypted

def decrypt(ct,k):
  keys = ks(k)
  state = str_split(ct)
  for b in range(len(state)):
    for i in range(rounds):
      rk = dec((state[b]))
      state[b] = to_chr(kx((rk), keys[i])) # xor with key
    print(state[b])
  return [ord(e) for es in state for e in es]
ct = to_str([63, 253, 213, 105, 250, 191, 55, 105, 226, 221, 223, 55, 55, 56, 55, 82, 146, 243, 159, 55, 55, 135, 213, 55, 94, 243, 55, 221, 94, 57, 226, 105, 196, 30, 213, 240, 91, 221, 152, 30, 213, 253, 37, 128])
print(decrypt(ct,key))
```
