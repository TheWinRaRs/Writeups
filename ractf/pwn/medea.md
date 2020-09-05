# Medea

OK so the binary got patched 4 times lol, I'll just pretend I solved it from the first one

The header reads: mCTZ, indicated the rest of the binary is compressed with 'zstandard'. We can use zstd to uncompress and read the image. It has 2 sections: scode and sin. SIN is ROM \(i thought it was input, causing me to delay my solve by at least 3 hours lmao\) and SCODE is the code of the program. Extracting the data from these blocks, we can use the specification at [https://github.com/Kantaja/MedeaCTF](https://github.com/Kantaja/MedeaCTF) to break down the logic of the program.

Accept input

Call function at 0x3E

The functions reads input into SMAIN \(general memory\) one char at a time until it reaches a newline, and then returns the length of the string by counting the iterations.

If length of the input != 0x0C, print "Incorrect length!" and die

Else, loop through each char of the input with the corresponding char in SIN.

Take the 2s complement of the SIN char.

XOR ~SIN with the input char

Output the result & 0xFF

And with 0xFF causes no changes to a value, so that can be ignored. We can skip the twos complement bit by prematurely XORing every value in SIN with 0xFF. Therefore the program becomes INPUT ^ SIN = OUTPUT.

However, we dont have any information about input or output beyond their lengths, EXCEPT that OUTPUT is wrapped in flag format. Therefore we can express it as

```text
INP: XXXXXXXXXXXX
OUT: ractf{XXXXX}
By reversing the function bit by bit, we can recover some of the input.
INP: 123412XXXXX4
OUT: ractf{XXXXX}
And finally, by extrapolating the pattern, we recover the full flag.
INP: 123412341234
OUT: ractf{C1Rc3}
```

## Flag: ractf{C1Rc3}

