# Cookie Library

NX, no PIE. The whole cookie thing is largely irrelevant so I'm not gonna comment on it.

It calls gets on rbp-0x50, opening an avenue for buffer overflow. We can do a ret2plt attack, calling puts@plt on puts@got in order to leak a libc address, specifically that of puts. Then, we can subtract the appropriate offset to get the libc base.

From there, it's a simple ret2libc attack. We call system\("/bin/sh"\) using pop rdi. The problem is, this doesn't seem to work. To make it work, we have to set rsi and rdx to 0. We don't have a pop rdx gadget inside of the binary, so it's impossible... right?

Wrong, actually. At this point in the exploit, we know the libc base, so we can use rop gadgets inside of the libc. So the full exploit is:

```text
1. use ret2plt to leak a libc address via the PLT and GOT
2. do poprdi + /bin/sh + pop rdx ; pop rsi + 0 + 0 + system in order to pop a shell
```

