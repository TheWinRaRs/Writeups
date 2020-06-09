# access=0000
##  Crypto

Basic CBC bit flipping - We're given ciphertext for `access=9999;`+ an expiry timestamp, and have to  provide an IV and ciphertext that decrypt to `acesss=0000`. https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'0000000000003d393939390000000000'%7D,'Standard',true)XOR(%7B'option':'Hex','string':'0000000000003d303030300000000000'%7D,'Standard',true)To_Hex('None',0)&input=NjA3MDcwOTllNDlhYjdmOWU5NTY2NWRjZTg0ZDI4NmVhNTI0Yzc1N2JhYmNjN2QyMWI1YTlhYWU0OTY1NGY1ZGNjNGU0ZjZkZGY5ZTk1OTUxNThkYmQyMzYyMDhjMmU1 
# `ractf{cbc_b17_fl1pp1n6_F7W!}`
