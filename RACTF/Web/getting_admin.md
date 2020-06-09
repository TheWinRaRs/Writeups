# Getting Admin
## Web

The next stage of the Quarantine series. I noticed that our session cookie was a JWT, signed with HS256. A vulnerability exists where these tokens can have their signing algorithm set to 'none' and their signature removed, and the web app will accept and process it. I used the highly useful [jwt_tool](https://github.com/ticarpi/jwt_tool) to resign it, editing my 'privilege' value from '1' to '10'. This allowed me access to the admin panel (more of a single page).

# `ractf{j4va5cr1pt_w3b_t0ken}`
