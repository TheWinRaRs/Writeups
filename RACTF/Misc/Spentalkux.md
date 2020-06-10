# Spentalkux
## Misc

The description simply read '🐍📦'. This (or just  googling the challenge name) leads us to the **Python** **Package** site PyPi, which had Spentalkux 13.37. I installed and ran this, and received this message:
> My creator left this behind but, I wonder what the key is? I don't know, but if I did I would say it's about 10 characters. Enjoy this.
>  Ztpyh, Iq iir'jt vrtdtxa qzxw lhu'go gxfpkrw tz pckv bc ybtevy...\*ffiieyano\*. New cikm sekab gu xux cskfiwckr bs zfyo si lgmpd://zupltfvg.czw/lxo/QGvM0sa6
>
The reference to a key of a given length made me think of Vigenère cipher. I pasted the message into [dcode.fr](https://dcode.fr) and set the known keylength to 10. 
>   Hello, If you're reading this you've managed to find my little... *interface*. The next stage of the challenge is over at https://pastebin.com/raw/BCiT0sp6 (key: SPENTALKUX)

This contained hex data, which gave us raw PNG data when decoded. The png contained binary  numbers translating to '_herring', and a message to look back in the past. I checked the version history of Spentalkux, and found and installed 0.9. This returned the message
`JA2HGSKBJI4DSZ2WGRAS6KZRLJKVEYKFJFAWSOCTNNTFCKZRF5HTGZRXJV2EKQTGJVTXUOLSIMXWI2KYNVEUCNLIKN5HK3RTJBHGIQTCM5RHIVSQGJ3C6MRLJRXXOTJYGM3XORSIJN4FUYTNIU4XAULGONGE6YLJJRAUYODLOZEWWNCNIJWWCMJXOVTEQULCJFFEGWDPK5HFUWSLI5IFOQRVKFWGU5SYJF2VQT3NNUYFGZ2MNF4EU5ZYJBJEGOCUMJWXUN3YGVSUS43QPFYGCWSIKNLWE2RYMNAWQZDKNRUTEV2VNNJDC43WGJSFU3LXLBUFU3CENZEWGQ3MGBDXS4SGLA3GMS3LIJCUEVCCONYSWOLVLEZEKY3VM4ZFEZRQPB2GCSTMJZSFSSTVPBVFAOLLMNSDCTCPK4XWMUKYORRDC43EGNTFGVCHLBDFI6BTKVVGMR2GPA3HKSSHNJSUSQKBIE`
After a long process of trial and error, I solved it. To save you some pain, here's a Cyberchef link: 
[Here](https://gchq.github.io/CyberChef/#recipe=From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true)Gunzip()From_Binary('Space')From_Binary('Space')From_Hex('Auto')From_Base85('!-u')&input=SkEySEdTS0JKSTREU1oyV0dSQVM2S1pSTEpLVkVZS0ZKRkFXU09DVE5OVEZDS1pSRjVIVEdaUlhKVjJFS1FUR0pWVFhVT0xTSU1YV0kyS1lOVkVVQ05MSUtONUhLM1JUSkJIR0lRVENNNVJISVZTUUdKM0M2TVJMSlJYWE9USllHTTNYT1JTSUpONEZVWVROSVU0WEFVTEdPTkdFNllMSkpSQVVZT0RMT1pFV1dOQ05JSldXQ01KWE9WVEVRVUxDSkZGRUdXRFBLNUhGVVdTTEk1SUZPUVJWS0ZXR1U1U1lKRjJWUVQzTk5VWUZHWjJNTkY0RVU1WllKQkpFR09DVU1KV1hVTjNZR1ZTVVM0M1FQRllHQ1dTSUtOTFdFMlJZTU5BV1FaREtOUlVURVYyVk5OSkRDNDNXR0pTRlUzTFhMQlVGVTNDRU5aRVdHUTNNR0JEWFM0U0dMQTNHTVMzTElKQ1VFVkNDT05ZU1dPTFZMRVpFS1kzVk00WkZFWlJRUEIyR0NTVE1KWlNGU1NUVlBCVkZBT0xMTU5TRENUQ1BLNFhXTVVLWU9SUkRDNDNFR05URkdWQ0hMQkRGSTZCVEtWVkdNUjJHUEEzSEtTU0hOSlNVU1FLQklF)

#### ractf{My5t3r10u5_1nt3rf4c3?}
