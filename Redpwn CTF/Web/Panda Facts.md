# Panda Facts

So, for this challenge, we need to set the "member" parameter in the json to something that is not 0, ideally 1.
idk all the techincal stuff but i just tried to inject stuff into the json
Since we still need valid json for it to work, I first gave the name a junk value, and then closed the quote, created a new member parameter, gave it the value 1, and then finally created a random parameter with a junk value to make sure it was valid json.
Final payload (just use this as a username)
`hi","member":1,"hi":"hi`

which gets you the flag: flag{t0ny_5uck5_47_w3b_l0l}

#### Flag: flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}
