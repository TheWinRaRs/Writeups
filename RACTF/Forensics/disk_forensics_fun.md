# Disk Forensics Fun
##  Forensics
We are given a hard drive image of a Linux Alpine system. Searching for recent files, we find 3 interesting ones. A PGP keypair, and a PGP encrypted file (/root and /home). 
`gpg --import 257-PRIVATE.PGP`
` gpg --output test.html --decrypt 197-NOTHINGH.ASC`
 Opening test.html gives us a moasai thing made out of coloured hexidecimal text. I then decoded with Cyberchef, which revealed it to be raw png data.
# `ractf{b4s1c_d1sk_f0r3ns1cs}`
