# difficult decryption

So i just followed the tutorial kek. i spent so long understanding what it meant so heres a summary of it

```text
1. compute prime factors of totient p in form p^k
2. find x modulo p^k (ill show later)
3. chinese remainder thereom!!!!!
4. compute shared key (other ** step3 % modulus)
5. xor and convert to hex then text!!!
tjctf{Ali3ns_1iv3_am0ng_us!}
```

did it this script \(after chinese remainder i got `64460789473481109991812750133942026256` alice - doesnt need to be prime because they cycle\)

```python
a = 491988559103692092263984889813697016406
msg = 12259991521844666821961395299843462461536060465691388049371797540470
c = [232042342203461569340683568996607232345,76405255723702450233149901853450417505]

at = 1
for i in a0:
    at *= phi(i)
print(at)

at0 = [[2**32],[3**15],[5**4],[7**3],[11],[13**2],[17],[19],[23],[29],[37],[53],[79],[109]]

for i in at0:
    temp = pow(c[0],at//i[0],a)
    for j in range(1,10000):
        if pow(pow(5,at//i[0],a),j,a) == temp:
            print(j,",",i[0],end = "),(")
            break
    else:
        print(j,"??")
```

