# A Musical Mix Up

So like the .mid file is a file playing a piano cover of Where Is My Mind (which is a banger btw go listen).

But like strings or binwalk shows nothing so confusion hit hard.

I scoured the internet for tools related to .mid file steganography and found one that converts a .mid to a .csv file. 

This was called midicsv and literally does what it says. 

So I ran that and it outputted a csv file with characters which looked like ASCII characters to the naked eye.

However there were 2 different streams of different ASCII characters.

I just opened up a site which converts ASCII to text and tried both streams.

The first one was nonsense but the second one had distinguishable features to it.

I  could see rac and f5soci3 which could be fsociety?

A Mr. Robot reference which ties into Where Is My Mind.

The track played on the .mid file. However not everything was readable. 

So I used another ASCII conversion site and I could see the flag clearly this time.
#### Flag: ractf{f50c13ty_l3vel_5t3g!}
