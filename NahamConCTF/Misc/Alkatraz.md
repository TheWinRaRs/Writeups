# Alkatraz

We can ls, there is flag.txt. No cat though. 

We'll have to use the bash builtin, read, instead.

Just do:

```bash
while read line; do echo $line; done < flag.txt
```
to execute a while loop that echoes all lines from flag.txt(note echo is a bash builtin too)
