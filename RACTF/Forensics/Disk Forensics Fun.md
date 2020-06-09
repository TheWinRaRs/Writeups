# Disk Forensics Fun

Searching for recent files, we find 3 interesting ones. A PGP keypair, and a PGP encrypted file (/root and /home). 


gpg --import 257-PRIVATE.PGP


gpg --output test.html --decrypt 197-NOTHINGH.ASC 


Opening test.html gives us a moasaicy thing made out of hex text. Decode with cyberchef, it's a png.


#### Flag:ractf{b4s1c_d1sk_f0r3ns1cs}
