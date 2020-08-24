# Homecooked


This is kinda more rev imo but whatever. 

We don't need to understand the main body of the script that much. 

What we need to know is that it gets to incredibly large numbers, at which point the two functions it uses - a and b - become much too slow and inefficient to be useful. 

Let's review the two functions:
What do they do? 

Function a simply iterates through all numbers between 2 and num - 1, and returns False if num % i == 0. Essentially, it checks if any numbers below a number are divisible by a number. What's that?

A prime checker.

We can just use `Crypto.Util.number.isPrime`, which is much more efficient.

As for b, it's much simpler. It just checks if the reverse of the string version of the number is the same as the number - checks if it's a palindrome. 
I just copied some more efficient code off stack overflow.
```python
def a(num):
    from Crypto.Util.number import isPrime
    return isPrime(num)  

def b(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if n == rev:
        return True
    return False
```
#### Flag: flag{pR1m3s_4re_co0ler_Wh3n_pal1nDr0miC}
