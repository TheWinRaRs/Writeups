# Countdown

The cookie is signed using flask. The page says 'Time is key'.

Using the `flask-unsign` utility, we can recover the secret key, 'Time'. We then resign data to move the 'end' date forwards.

```text
flask-unsign --sign --cookie "{'end': '2020-06-13 16:59:59+0000'}" --secret 'Time'
```

Sending the resulting cookie gives us the flag.

## rgbCTF{t1m3\_1s\_k3y\_g00d\_j0k3\_r1ght}

