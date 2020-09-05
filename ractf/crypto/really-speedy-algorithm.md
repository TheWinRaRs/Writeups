# Really Speedy Algorithm

Essentially a scripting challenge. You'll be given all sorts of parameters and need to calculate the missing one. Instead of going through every possible solution, which would've been really excruciating, I went through this approach -

Create a function that solves for a value.

The function's logic is as follows:

if we want a value that's already defined, just return it

if we want n, call ourself to solve p and q, then multiply

if we want ct, call ourself to solve n, then do pt^e mod n

if we want pt, call ourself to solve d and n, then do ct^d mod n

if we want d, call ourself to solve p and q,compute phi, then return inverse\(e,phi\)

if we want p, or q, then:

pretend p is the prime we have and q is the prime we want

if we have n, return n // p

if we have phi, return \(phi // \(p - 1\)\) + 1

if all else fails and we have e and d, use Crypto.PublicKey.RSA to compute p and q via n, e and d

```python
import socket
from Crypto.Util.number import inverse, GCD
from Crypto.PublicKey import RSA
IP = '95.216.233.106'
PORT = 62467
def dosolve(val):
    global cur
    if val in cur.keys():
        return cur[val]
    if val == 'q' or val == 'p':
        # Prime solving
        # Pretend the prime we want is q and the prime we have is p every time for simplicity.
        if 'q' in cur.keys():
            cur['p'] = cur['q']
        if 'n' in cur.keys():
            return cur['n'] // cur['p']
        elif 'phi' in cur.keys():
            return (cur['phi'] // (cur['p'] - 1)) + 1
        elif 'e' in cur.keys() and 'd' in cur.keys():
            key = RSA.construct((cur['n'],cur['e'],cur['d']))
            primes = [key.p,key.q]
            primes.remove(cur['p'])
            return primes[0]
    elif val == 'd':
        cur['p'] = dosolve('p')
        cur['q'] = dosolve('q')
        phi = (cur['p'] - 1) * (cur['q'] - 1)
        d = inverse(cur['e'],phi)
        return d
    elif val == 'n':
        cur['p'] = dosolve('p')
        cur['q'] = dosolve('q')
        return cur['p'] * cur['q']
    elif val == 'ct':
        cur['n'] = dosolve('n')
        return pow(cur['pt'],cur['e'],cur['n'])
    elif val == 'pt':
        cur['d'] = dosolve('d')
        cur['n'] = dosolve('n')
        return pow(cur['ct'],cur['d'],cur['n'])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.setblocking(0)

buffer = b''
cur = {}
while True:
    # Read until a prompt or line break
    try:
        chunk = s.recv(4096)
        buffer += chunk
        print(chunk.decode(), end='')
    except BlockingIOError:
        pass

    if b'\n' not in buffer and not buffer.endswith(b': '):
        continue

    # Grab the oldest line
    buffer = buffer.split(b'\n', 1)
    if len(buffer) == 1:
        line, buffer = buffer[0], b''
    else:
        line, buffer = buffer

    # Llines start with [<code>]
    if line[:1] != b'[':
        continue

    # Use slicing not indexing because indexing bytes returns ints
    mode = line[1:2]
    if mode == b'*':
        ...
    elif mode == b'c':
        cur = {}
    elif mode == b':':
        important = line[3:].decode().split(": ")
        value = int(important[1])
        cur[important[0].strip()] = value
    elif mode == b'!':
        print(line)
    elif mode == b'?':
        needed = line[3:].decode().split(": ")[0].strip()
        if needed in cur.keys():
            s.send(str(cur[needed]).encode() + b'\n')
            continue
        val = dosolve(needed)
        print(val)
        print(cur)
        s.send(str(val).encode() + b'\n')
    else:
        ...
```

