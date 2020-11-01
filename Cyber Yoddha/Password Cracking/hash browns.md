# hash browns
jammy made a list of french cities in tescos, then hash cracking
```py
from hashlib import sha512
import itertools
target = "F3899973D90D9EBB3A03ABC143B293CD33CFD688CB949AE1FBA61ACAB0D3D6220948AB3C35E00AF9D9497484B666D7FEA9D7673E2FC6AE463936C7B797FB3AF0".lower()
cities = open('cities.txt').read().split('\n')

def generate_strings(length):
    chars = "0123456789"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

for numberlen in range(1, 8):
    for c in cities:
        for item in generate_strings(numberlen):
            if sha512(c.encode() + item.encode()).hexdigest() == target:
                print(c + item)

    print(numberlen)
```
#### Flag: CYCTF{grenoble38100}
