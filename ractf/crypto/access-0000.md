# Access=0000

Basic CBC bit flipping - We're given ciphertext for `access=9999;`+ an expiry timestamp, and have to provide an IV and ciphertext that decrypt to `acesss=0000`.

[https://gchq.github.io/CyberChef/\#recipe=From\_Hex\('Auto'\)XOR\(%7B'option':'Hex','string':'0000000000003d393939390000000000'%7D,'Standard',true\)XOR\(%7B'option':'Hex','string':'0000000000003d303030300000000000'%7D,'Standard',true\)To\_Hex\('None',0\)&input=NjA3MDcwOTllNDlhYjdmOWU5NTY2NWRjZTg0ZDI4NmVhNTI0Yzc1N2JhYmNjN2QyMWI1YTlhYWU0OTY1NGY1ZGNjNGU0ZjZkZGY5ZTk1OTUxNThkYmQyMzYyMDhjMmU1](https://gchq.github.io/CyberChef/#recipe=From_Hex%28'Auto'%29XOR%28%7B'option':'Hex','string':'0000000000003d393939390000000000'%7D,'Standard',true%29XOR%28%7B'option':'Hex','string':'0000000000003d303030300000000000'%7D,'Standard',true%29To_Hex%28'None',0%29&input=NjA3MDcwOTllNDlhYjdmOWU5NTY2NWRjZTg0ZDI4NmVhNTI0Yzc1N2JhYmNjN2QyMWI1YTlhYWU0OTY1NGY1ZGNjNGU0ZjZkZGY5ZTk1OTUxNThkYmQyMzYyMDhjMmU1)

## ractf{cbc\_b17\_fl1pp1n6\_F7W!}

