# Robot Takeover


```py
url= "http://challenge.ctf.games:31879/robots.txt"
aurl= "http://challenge.ctf.games:31879/"
import urllib.request

def get(url, ua):
  req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': ua
    }
  )
  return req

flag = ["" for i in range(35)]
while "" in flag:
  with urllib.request.urlopen(url) as response:
     html = response.read()
     lines = html.decode().split("\n")
     for line in lines:
       if "User-agent:" in line:
         ua = line[12:]
       if "Disallow: " in line:
         thing = line[10:]
         theurl = aurl + thing
         req = get(theurl,ua)
         with urllib.request.urlopen(req) as response:
           resp = response.read().decode()
           if "REJOICE" in resp:
             print(resp, line)
             thonk = resp.split("INDEX ")
             filename = thing[1:]
             a1 = int(thonk[1].split(" IS")[0])
             a2 = int(thonk[2].split(" IN")[0])
             flag[a1] = filename[a2]
             print(flag)

print("".join(flag))
```
