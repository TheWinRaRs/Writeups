# home rolled

So after deobfuscating the script (which i didnt rly needed to) i found it was encrypted with a otp of random order of range(256). so then i thought "kek how can i break otp" but then i realised it never repeats itself. i also knew that it started with "tjctf{" and ended with "}". i created a list of possible values left and used that for each position of the flag. this gave me a bunch of characters possible for that position. i just needed to repeat it until there was 1 char left (connected with vpn cus doxx). i did it with this script.
#### tjctf{n3v3r_r0LL_ur_0wn_cryptOMEGALUL}
