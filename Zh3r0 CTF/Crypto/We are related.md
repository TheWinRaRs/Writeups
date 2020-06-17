# We are related

Connect to the server. 
Besides exiting, there's two options - get the public key, 
and encrypt data. 

Let's get the publickey and parse it.
```python
rom Crypto.PublicKey import RSA
key = RSA.import_key("""-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAl/DEzNkDSy545CVnRDY6
MvnY3uT9AqXvUawLjvPxkpGFvjNZgXUZDXz4d+OM+kI0wCitG/qKKyALNBCRV4H1
Ff032MF4M83DZauv9mekDRYTHt1kc3yjXGgkDKrbwx/52oK1zzjDpdL35+0DGrCV
MuM6UUGmwULkt9pwkltaQ7CnK/mD8r9/kxCvYrsOdXKfG7oa6M8jmJ2Fg8KI30K7
BNLBQnrHEd+gk9cbeZO2EPfCgpeRBIkpN/m+wCaVeF4MhvHAqO7WY8HWGnWOXTvX
s/s38/18neVZpi6sb+Xzd5bS3MXF6LAYnpsPFtlZQwkef0isv+fIbRehCBxOOXMO
cwIBAw==
-----END PUBLIC KEY-----
""")
e = key.e
n = key.n
print(key.e)
print(key.n)
```
the output is e = 3 and n = 19180711545893176513037550390323379574821852830665661812056678865741809891967598330424432450065638550340708416772232861627803383996685973692319978144111094705678356718069839745329804369923049623077146724976343425793942969144731442443607177966505595110345695314223998207352543996470777991272166737723490287258351016452097039979125039319504321174407700539531877444075872453220474913463319033875264101011295681676774076367210997858399851393634010112304767318681335454946488666538950765836709367621997962434256967765320251658524109362889423421160554230180542246491892887129152380892721807921025298941063392821275387956851

Then, there's encrypt. Our message is appended to the flag, then encrypted using the publickey. This makes it vulnerable to franklin-reiter's related message attack, in which RSA with low exponents can be attacked if you have two messages, C1 and C2, such that dec(C1) = f(dec(C2)) where f is a function of form f(x) = ax + b, and b and a are non-zero. If we ask the server to encrypt an empty message(thus getting the encryption of the flag), and then 'A', we now have an encryption of the flag(lets call this C2) and an encryption of the flag + 'A', which is 256*flag + 0x41.
So..
We now have the encryption of the flag, and the encryption of f(flag), where f(x) = 256x + 65

Using this, we can execute franklin reiter's related message attack. I copied some sage code and included variables. You can run the sage code on the sage cell server, https://sagecell.sagemath.org/. The output will be the hex encoding of the message, which decodes to "RSA is secure and all but the only thing I want to say is zh3r0{Hey_y0u_Sh0u1dn't_S3nd_r3l4ted_m3ssag3s_0r_h4v3_shot_p4ddings_wh3n_e_1s_sm411!!!!!}."
Sage script below.
