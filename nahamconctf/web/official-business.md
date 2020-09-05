# Official business

Go to `/robots.txt`.

Look at source code

```python
def load_cookie():

    cookie = {}
    auth = request.cookies.get("auth")
    if auth:

        try:
            cookie = json.loads(binascii.unhexlify(auth).decode("utf8"))
            digest = cookie.pop("digest")

            if blah():#...performs check
                return False, {}
        except:
            pass
#...more code...
def index():
    ok, cookie = load_cookie()
    if not ok: return abort(403)
    return render_template(
        "index.html",
        user=cookie.get("user", None),
        admin=cookie.get("admin", None),
        flag=FLAG)
    return True, cookie
```

So just make cookie exist but somehow error out to skip to end.

I did this by not including digest val in cookie

reload page and...

## flag{did\_this\_even\_pass\_code\_review}

