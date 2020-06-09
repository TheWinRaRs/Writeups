# Entrypoint

We can see in HTML comments of the web page: 
```
html
<!-- In case I forget: Backup password is at ./backup.txt -->
```
However we get a 403 Forbidden if we try to access this file with `/backup.txt`

We can see that the CSS file is included with `href="/static?f=index.css"`

So if we go to `/static?f=backup.txt`, we get the credentials for the develop user.

#### Flag: ractf{developerBackupCode4321}
