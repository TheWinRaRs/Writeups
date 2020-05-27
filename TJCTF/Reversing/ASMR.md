# ASMR

( https://gist.github.com/bobbo/e1e980262f2ddc8db3b8 for help)
So we download the file, and we find that it's pure assembly written in intel syntax, nice. Let's compile it:
nasm -f elf64 -o asmr.o asmr.asm
ldd -o asmr asmr.o
When we run it, we don't get anything back. Odd. Lets see what's in the assembly.
I decided to reverse all the assembly so that we can get a good picture of what's happening. 
Basically, in main, it's creating a socket, setting some options for the socket, binding the connection to port 1337, 
listening on any address, then accepts the connection. Once we connect, it sends "Enter Password:".
The program then reads our input, and checks to see whether it's 17 chars (16 + null byte). 
If our input isn't 16 chars + null byte, it chucks us to label5, which is basically output "Nope" and then end the connection.
So we don't want that. We see that label2 compares our last char to null byte. 
Whilst our input != a null byte, it xors it with key 0x69 (105 in decimal) (that's what label1 does).
Label2 then checks to see if that's the password, and if it's correct, it spits out 56333 chars of hex at us. 
If we get the hex that it moves to the rax register (0x360c1f0605360c1e) and (0x0c0c10361b041a08), xor it with key 0x69 and reverse, 
we get "we_love_asmr_yee". Input that as the password, and the hex gets spit out.
If we restart it all again but save to a file, that's a lot nicer to work with. 
The flag isn't in the strings, but if we take a look at it in ghex, we see a whole load of things.
Removing the "Enter password:" and looking at the file headers, we see that it's a .ogg file.
Save the file as that, open it in an audio player,
and we get "The flag is tjctf{Bravo Uniform Bravo 6 Lira Echo _ Whiskey Romeo 4 Pop _ Pop 0 Pop}" 
That's a very long flag, so probably not.
Using the hint they gave us (NATO Phonetic Alphabet), we can swap the words for letters and we get a nice message from the team,
as well as  tjctf{s0m3_n1c3_s0und5_for_you!!!}
