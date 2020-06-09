# Spentalkux

The clue is 'python package' in emojis.  
Googling the name gives us a PyPi package, which I can install and run with `python -m spentalkux`.  
This says:  
```
My creator left this behind but, I wonder what the key is? I don't know, but if I did I would say it's about 10 characters.
```
Enjoy this.  
```
Ztpyh, Iq iir'jt vrtdtxa qzxw lhu'go gxfpkrw tz pckv bc ybtevy... *ffiieyano*. New cikm sekab gu xux cskfiwckr bs zfyo si lgmpd://zupltfvg.czw/lxo/QGvM0sa6
```
I guessed vignere, and used dcode.fr to bruteforce with 10 chars, getting a link to: https://pastebin.com/raw/BCiT0sp6  
This contained hex data, which gave us a png when decoded.  
The png contained binary for 'red_herring', and a message to look back in the past.  
I checked the version history of spentalkux, and found and installed 0.9.  
This gave some text, which I put through a decoder here:  
https://gchq.github.io/CyberChef/#recipe=From_Base32(%27A-Z2-7%3D%27,true)From_Base64(%27A-Za-z0-9%2B/%3D%27,true)Gunzip()From_Binary(%27Space%27)From_Binary(%27Space%27)From_Hex(%27Auto%27)From_Base85(%27!-u%27)&input=SkEySEdTS0JKSTREU1oyV0dSQVM2S1pSTEpLVkVZS0ZKRkFXU09DVE5OVEZDS1pSRjVIVEdaUlhKVjJFS1FUR0pWVFhVT0xTSU1YV0kyS1lOVkVVQ05MSUtONUhLM1JUSkJIR0lRVENNNVJISVZTUUdKM0M2TVJMSlJYWE9USllHTTNYT1JTSUpONEZVWVROSVU0WEFVTEdPTkdFNllMSkpSQVVZT0RMT1pFV1dOQ05JSldXQ01KWE9WVEVRVUxDSkZGRUdXRFBLNUhGVVdTTEk1SUZPUVJWS0ZXR1U1U1lKRjJWUVQzTk5VWUZHWjJNTkY0RVU1WllKQkpFR09DVU1KV1hVTjNZR1ZTVVM0M1FQRllHQ1dTSUtOTFdFMlJZTU5BV1FaREtOUlVURVYyVk5OSkRDNDNXR0pTRlUzTFhMQlVGVTNDRU5aRVdHUTNNR0JEWFM0U0dMQTNHTVMzTElKQ1VFVkNDT05ZU1dPTFZMRVpFS1kzVk00WkZFWlJRUEIyR0NTVE1KWlNGU1NUVlBCVkZBT0xMTU5TRENUQ1BLNFhXTVVLWU9SUkRDNDNFR05URkdWQ0hMQkRGSTZCVEtWVkdNUjJHUEEzSEtTU0hOSlNVU1FLQklF
#### Flag: ractf{My5t3r10u5_1nt3rf4c3?}
