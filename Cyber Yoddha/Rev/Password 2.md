# Password 2
It does some scrambling in python, just kinda copy the scrambling and reverse the statements(e.g newpass[i] = password[32-i] becomes password[32-i] = newpass[i])

#### Flag: CYCTF{ju$t_@_l177l3_scr@mbl3_f0r_y0u_t0_d3c0d3}
```py
newpass = list("CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m")
password = newpass[:]
for i in range(9):
    password[i] = newpass[i]
for i in range(9,24):
    password[32-i] = newpass[i]
for i in range(24,47,2):
    password[70-i] = newpass[i]
for i in range(45,25,-2):
    password[i] = newpass[i]
print(''.join(password))
```
