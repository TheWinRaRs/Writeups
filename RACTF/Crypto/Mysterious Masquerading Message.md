# Mysterious Masquerading Message.md

The OpenSSH private key is actually not a private key and is simply just base64. We decode it to get a long useless message and 2 hex strings. 
If we decode these hex strings we get,
`ineedtoopenlocks` and `initialisation12`
Decoding the binary gets us a long hex string.
Looking at initialisation, I immediately thought of AES. Since an IV is provided, we can assume it is AES-CBC, so I just used cyberchef to decrypt and get the flag.

#### Flag: ractf{3Asy_F1aG_0n_aEs_rAcTf}
