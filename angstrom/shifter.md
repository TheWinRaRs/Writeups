# Shifter

```python
import socket
import re
fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 8, 3, 11, 14, 25, 13, 12, 25, 11, 10, 21, 5, 0, 5, 5, 10, 15, 25, 14, 13, 1, 14, 15, 3, 18, 21, 13, 8, 21, 3, 24, 1, 25, 0, 25, 25, 24, 23, 21, 18, 13]
def fibshift(num, msg):
    list1 = [chr(ord(i)+fibo[num]) for i in msg]
    list2 = [chr(ord(j)-26) if ord(j)>90 else j for j in list1]
    return "".join(list2)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('misc.2020.chall.actf.co', 20300))
for i in range(0, 50):
    message = clientsocket.recv(2048)
    task = [k for k in message.splitlines() if "Shift" in k][0]
    clientsocket.send(fibshift(int(re.search('by n=(.*)', task).group(1)), re.search('Shift (.*) by', task).group(1)) + "\n")
print(clientsocket.recv(2048))
```

## actf{h0p3\_y0u\_us3d\_th3\_f0rmu14-1985098}

