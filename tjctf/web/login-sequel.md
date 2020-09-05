# Login sequel

Set username to "admin'/\*" and the password to whatever this is so the command executed is

```sql
"SELECT username, password FROM `userandpassword` WHERE username='admin/*' AND password='<md5 HASH object @ 0x00000151246A95F8>'"
/* is a comment so everything after that is ignored.
```

EZ

## flag is tjctf{W0w\_wHa1\_a\_SqL1\_exPeRt!}

