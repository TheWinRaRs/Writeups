# Katycat

Download the file, run zsteg on it and you'll get a pastebin link. `https://pastebin.com/hvgCXNcP`.

Visit that and you'll find base64 text that decodes into a zip file.

Save the zip file and open it but its password protected.

So run zip2john and get the hash and dictionary attack it with `rockyou.txt` You'll get a password of kitkat.

After catting flag.txt run a ROT47 decryption on it and you get.

## Flag: zh3r0{1sn7\_st3g4n0\_e4sy}

