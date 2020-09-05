# AP lab: Comp Sci Principles

Download -&gt; read file -&gt; We've been provided with a java file

Upon some basic looking, we can see that the input has to be 18 chars - `if (inp.length() != 18) { System.out.println("Input is incorrect") }` .

We can also see - `if (inp.equals("inagzgkpm)Wl&Tg&io")) { System.out.println("Input if the flag") }` . So we know our input, and that string is 18 chars. Perfect.

We also see that - `inp = shift( shift(inp) )` , so now time for the reversing.

All `shift()` does is gets a character in a string and then minuses i from that, and then stores it in a ret variable. So doing a bit of changing a minus to a plus, we manage to get a new string from that - `"iocj~lqwu2aw2au5y\x80"` \(\x80 isn't an ascii char\) - We can remove that \x80, as we know that it's going to be }.

I couldn't code this in python, so I turned to a online java compiler, and performed `shift2()` on that string, but again, taking a plus as a minus for reversing it.

That should return the flag, and you just pad it with the } that we took out earlier \(\x80\)

## Flag: flag{intr0\_t0\_r3v}

Python rev for shift

```python
a = ["i","n","a","g","z","g","k","p","m",")","W","l","&","T","g","&","i","o"]

def rev_shift(a):
    ret = ""
    tmp = ""

    for i in range(len(a)):
        tmp = (ord(a[i]) + i)
        ret += chr(tmp)

    return ret

print(rev_shift(a))
```

Java rev for shift2

```java
public class ctf_rev{  
public static void main(String args[]){  
String input = "iocj~lqwu2aw2au5y";
String ret = "";
for (int i = 0; i<input.length(); i++){
    ret += (char)(input.charAt(i) - Integer.toString((int)input.charAt(i)) .length());
}
System.out.println(ret);
}}
```

