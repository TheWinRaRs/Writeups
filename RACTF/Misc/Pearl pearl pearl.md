# Pearl pearl pearl

Upon connecting to the server, it just sends lots of lines of `ctf{pearlpearlpearl}`.  
Nothing that interesting. I decided to script this to see if it was like some challenges we had seen in previous ctfs where we required speed, but this was not the case. I did however, notice something very interesting you wouldn't see on a terminal from doing nc - between lines of `ctf{pearlpearlpearl}`, it didn't just use newlines, it used `\r` too.  
In fact, it alternated between the two in a non-regular pattern. I decided to strip all `ctf{pearlpearlpearl}` from the output of the server and get the pure \r and \n. Then, I converted \r to 0 and \n to 1 and attempted to convert from binary.  
This worked, and yielded the flag  
#### Flag: ractf{p34r1_1ns1d3_4_cl4m}.
