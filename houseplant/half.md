# Half

For a while i was stumped. I split the ciphertext into two, took every other character, did weird xor, base64 decoding, taking every other nibble, taking every other bit - no dice.

Eventually, I decided to think more into the challenge title. They wouldn't put it in morse code for no reason, right? I began to look up special morse code ciphers, and then I thought.. a half is a fraction, right?

Fractionated morse code.

Paste in the ciphertext to a fractionated morse code decoder and you'll get the string `RTCPTW0GALLONSOFH4LFMAK3WH0LEM1LK E`. I think the E is either a mistake or weirdness with the site I used. Anyways, turn the rtcp into lowercase and wrap the rest in curly brackets to get your golden flag.

## rtcp{TW0GALLONSOFH4LFMAK3WH0LEM1LK}

