# Admin Attack

This is the same principle as Baiting. This time we need to log into the admin user.

From the list of users we found with the devloper credentials, `jimmyTehAdmin` is the account we need to log in to.

We can use a similar payload to before (this challenge is more resitant to SQLMap)

```' OR username='jimmyTehAdmin' -- ```

#### Flag: ractf{!!!4dm1n4buse!!!}
