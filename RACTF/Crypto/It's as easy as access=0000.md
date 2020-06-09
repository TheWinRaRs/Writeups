# It's as easy as access=0000

Basic CBC bit flipping - We're given ciphertext for access=9999;....... and just have to xor the iv with access=9999 then access=0000 and send back the modified IV.


https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'0000000000003d393939390000000000'%7D,'Standard',true)XOR(%7B'option':'Hex','string':'0000000000003d303030300000000000'%7D,'Standard',true)To_Hex('None',0)&input=NjA3MDcwOTllNDlhYjdmOWU5NTY2NWRjZTg0ZDI4NmVhNTI0Yzc1N2JhYmNjN2QyMWI1YTlhYWU0OTY1NGY1ZGNjNGU0ZjZkZGY5ZTk1OTUxNThkYmQyMzYyMDhjMmU1


#### Flag: ractf{cbc_b17_fl1pp1n6_F7W!}
