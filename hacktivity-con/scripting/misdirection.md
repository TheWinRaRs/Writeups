# Misdirection

So uh will noticed that each of the urls it redirects you to has a character of the flag in the http body so just script grabbing the urls and then script curling them

```python
import os
import re
url = "http://jh2i.com:50011/site/flag.php"
urls = []
while 'sorry' not in url:
    data = os.popen(f"curl -Is {url}").read()
    url = "http://jh2i.com:50011" + re.findall("Location: (.*)",data)[0]
    print(url)
    urls.append(url)
print(urls)
flag = ''
for url in urls:
    data = os.popen(f"curl {url} 2>/dev/null").read()
    if data:
        flag += data[-2]
        print(flag)
```

## Flag: flag{http\_302\_point\_you\_in\_the\_right\_redirection}

