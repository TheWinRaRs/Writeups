# itsy bitsy

Theres a flaw in code that means every nth bit results in 1,

which can be unxored later \[used primes for efficiency - doesnt repeat bit\]

```python
import socket
host = "2020.redpwnc.tf"
port = 31284
ip = "35.231.164.133"#socket.gethostbyname(host)
def crack():
    template = [x for x in "-"*500]
    for i in primes: # use ur own primes
        a = server(i-1,i)
        for k,l in enumerate(str(a)):
            if k%(i) == 0:
                template[k] = str(int(l) ^ 1)
        print("".join(template))
def server(i,j):
    s = socket.socket()
    s.connect((ip, port))
    a = s.recv(1024)
    print(a,i)
    s.send((str(i)+"\n").encode())
    a = s.recv(1024)
    print(a,j)
    s.send((str(j)+"\n").encode())
    out = s.recv(1024).decode().split(" ")[1]
    print(out)
    return out
crack()
```

get every 7 bytes to get...

## flag{bits\_leaking\_out\_down\_the\_water\_spout}

