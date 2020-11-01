# The Shebang series

0.)
```
ssh shebang0@cyberyoddha.baycyber.net -p 1337
(password shebang0)
$ ls -alt
total 12
drwxr-xr-x 1 root     root 4096 Oct 30 07:07 ..
dr-x------ 1 shebang0 root 4096 Oct 30 07:07 .
-rw-r--r-- 1 root     root   33 Oct  6 00:26 .flag.txt
$ cat .flag.txt
```
#### Flag: CYCTF{w3ll_1_gu3$$_b@sh_1s_e@zy}

<hr>

1.)
```
$ cat flag.txt | grep "CYCTF"
```
#### Flag: CYCTF{w3ll_1_gu3$$_y0u_kn0w_h0w_t0_gr3p}

<hr>

2.)

forgot how to do it there is loads of files and you do something to get the flag

#### Flag: CYCTF{W0w_th@t1337@_l0t_0f_f1l3s}

<hr>

3.)

says 2 files are the same so we just run diff
```
diff file.txt file2.txt
```
shows a massive list of differences we go down and the flag is on each line
#### Flag: CYCTF{SPOT_TH3_D1FF}

<hr>

4.)

`openssl base64 -in flag.png -out flag.txt`
copy the b64 and then `base64 -d flag.txt > flag.png`
open the image and the flag is there

#### Flag: CYCTF{W3ll_1_gu3$$_th@t_w@s_actually_easy}

<hr>

5.)
```
find / -perm -u=s -type f 2>/dev/null

/var/cat
```
for some reason the flag was in /etc/passwords/shebang6 so.
```
/var/cat /etc/passwords/shebang6
```
#### Flag: CYCTF{W3ll_1_gu3$$_SU1D_1$_e@$y_fl@g$}
