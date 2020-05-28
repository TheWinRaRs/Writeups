# Sizzle

Translating from morse code it doesn't seem right.. a bunch of numbers and mathematical operators in a weird order. The hint says "is it really what you think it is" or something similar, so it seems obvious that what seemed to be morse code isnt actually morse code.

The challenge is called sizzle, and talks about bacon... what if it's a bacon cipher?

I used subsitution to change . to 0 and - to 1, and then put it through a bacon cipher decoder. This gave me the expression `BACONBUTGRILLEDANDMORSIFIED`. I put this into all lowercase, separated the words with underscores


Cyberchef link: https://gchq.github.io/CyberChef/#recipe=Substitute(%27.-%27,%2701%27)Bacon_Cipher_Decode(%27Standard%20(I%3DJ%20and%20U%3DV)%27,%270/1%27,false)To_Lower_case()&input=Li4uLi0gLi4uLi4gLi4uLS4gLi0tLi0gLi0tLi4gLi4uLi0gLS4uLS0gLS4uLS4gLi4tLS4gLS4uLi4gLi0uLi4gLi0uLS4gLi0uLS4gLi4tLi4gLi4uLS0gLi4uLi4gLi0tLi4gLi4uLS0gLi0uLS0gLi0tLi0gLS4uLi4gLS4uLi0gLi0uLi4gLi4tLi0gLi0uLi4gLi4tLi4gLi4uLS0
#### rtcp{bacon_but_grilled_and_morsified}
