# Secret Array 

If you request the sums of 0 1, 1 2, and 2 0, you can sum them and divide to get the sum of 0, 1 and 2. 

Then subtracting one of the above from this lets you find 0, 1 and 2, from which you can ask for 2 3 to get 3, etc. 

Script below. 

```python
import socket
socket = socket.socket()
socket.connect(('secretarray.fword.wtf', 1337))
socket.recv(2048)
def recv():
    while True:
        a = socket.recv(2048).decode('ASCII')
        if a != '\n':
            return a
socket.send(b'0 1\n')
a=[]
a.append(int(recv()))
socket.send(b'1 2\n')
a.append(int(recv()))
socket.send(b'2 0\n')
a.append(int(recv()))
s=sum(a)//2
b=[s-a[1], s-a[2], s-a[0]]
print(b)
for i in range(2, 1336):
    socket.send(f'{i} {i+1}\n'.encode('ASCII'))
    b.append(int(recv())-b[-1])
    print(f'{i+1} - {b[-1]}')
socket.send(("DONE "+" ".join(str(i) for i in b)+'\n').encode('ASCII'))
socket.recv(2048)
print(socket.recv(2048))
```
