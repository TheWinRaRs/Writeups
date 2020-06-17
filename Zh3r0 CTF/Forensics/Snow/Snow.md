# Snow.md

So download the file. 

Unzip it and notice the challenge name is Snow so use stegsnow. 

Once extracted you get a file called chall.txt which presumably you use stegsnow on. 

However theres hidden directories. If you go down it you find `.flag.txt` which is a fake flag but if you go further you find `.secret.txt` which is the password. 

So run `stegsnow -C -p "welc0me_to_zh3r0_ctf" chall.txt` and you get the flag.

#### Flag: zh3r0{i5_it_sn0w1ng?}
