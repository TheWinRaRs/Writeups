# Twis Twis Litlle Star

https://github.com/tna0y/Python-random-module-cracker 

(title hints at mersenne twister, which is what python random uses)

script below:

```python
from pwn import *
from randcrack import RandCrack

rc = RandCrack()

s = remote("twistwislittlestar.fword.wtf", 4445)
print(s.recvline())
print(s.recvline())
print(s.recvline())
print(s.recvline())
print(s.recvline())
print(s.recvline())
d1 = int(s.recvline().decode().split(" : ")[1][:-1])
d2 = int(s.recvline().decode().split(" : ")[1][:-1])
d3 = int(s.recvline().decode().split(" : ")[1][:-1])
print(d1,d2,d3)
rc.submit(d1)
rc.submit(d2)
rc.submit(d3)
print(s.recvline())
for i in range(621):
  s.recvline()
  s.sendline("1")
  s.recvline()
  d = int(s.recvline().decode().split(" : ")[1][:-1])
  print(d,i)
  rc.submit(d)
  s.recvline()
p = []
for i in range(100):
  p.append(rc.predict_randrange(0, 4294967295))
print(p)
s.interactive()
```

#### Flag: FwordCTF{R4nd0m_isnT_R4nd0m_4ft3r_4LL_!_Everyhthing_is_predict4bl3_1f_y0u_kn0w_wh4t_Y0u_d01nGGGG}
