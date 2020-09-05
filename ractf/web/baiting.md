# Baiting

If we log in with the credentials from Entrypoint, we can see a list of users.

One of these is called `"loginToGetFlag"`, so we'll try to log into this one.

We get a SQL error if we put a ' so we can try SQL Injection payloads.

We can use the payload:

`loginToGetFlag' --`

to log into this user - and we get the flag.

## Flag: ractf{injectingSQLLikeNobody'sBusiness}

