# Password 3
The flag is just XORed with 0x55 and then base64 encoded.

We can decode this with cyberchef.

https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'Hex','string':'55'%7D,'Standard',false)&input=Rmd3V0FSTXVGMlVoUFFvdFpTY0tGVHN4Q2pjVkptWUtZMkZxQ2lFOUZTRW1DakpsTVRrc0tBPT0

#### Flag: CYCTF{B0th_x0r_@nd_b@s3_64?_th@ts_g0dly}
