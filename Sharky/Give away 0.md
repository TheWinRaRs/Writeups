# Give away 0

Simple buffer overflow. There is a function win_func that calls system on a global variable. We can read this global variable and find it's value is `/bin/sh` - it pops a shell for us.

In the function vuln, it reads `0x32` bytes into a buffer at `rbp-0x20`. This allows us to overwrite the return address with the address of winfunc.

So our exploit is `0x28 bytes of junk + address of win_func`.
