# Uncipher Me

Looking at the ct file, it starts with "gAAAAAB"

This reminded me of the HTB challenge Decode Me!!!, which used fernet decryption as the first step.

Key1 and Key3 were useless, but applying ROT47 to key2 with key 47 gave us:

key: iQZijGdoX0hepv2wnFZOUsTWU-v6xyGWyqSan\_p75CE=

Here's another key for the encryption.

if you are a good cryptographer you can identify the common symmetric encryption.

giving us our key for fernet.

Then, I just plugged the CT and key into a fernet decoder \([https://asecuritysite.com/encryption/ferdecode](https://asecuritysite.com/encryption/ferdecode)\) to get the flag.

## Flag: zh3r0{Symm3tric\_3ncrypti0n\_i5\_5tr0ng}

