# Quarantine

We are presented with a login page. As this was a low-rated challenge, I began by testing basic SQLi.

Entering `' or 1=1; -- -` in the username field returned the message 'You are trying to login as multiple users'.

From this, I determined that the injection was sucessful, but as this query returned multiple users the web app was rejecting it.

I simply edited the payload to be `' or 1=1 limit 1; -- -`, and I got access

## ractf{Y0u\_B3tt3r\_N0t\_h4v3\_us3d\_sqlm4p}

