# Differences

A Java file where some of the bytes have been corrupted to non-printable values. I went through and corrected it:
```java
import java.util.*;
public class DifferenceTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
        int answer = num1 - num2;
        System.out.println("The difference is: " + answer);
    }
}
```
Then used:
```python
f1 = open('DifferenceTest.java', 'rb').read()
f2 = open('Corrected.java', 'rb').read()
f1 = list(f1)
f2 = list(f2)

for one, two in zip(f1,f2):
    if one != two:
        print(chr(one-two), end='')
print('')
```
This takes the difference between any non-matching bytes and prints them as ascii

rgbCTF{tr1pl3_m34n1ng}
