# Eccentric Encryption Engima

Let's start from scratch - run the binary. It'll complain to us that we don't have some python library called memecrypt installed. That's odd.. why does it demand a python library if its an ELF file? More on this later. We can install with ```python3 -m pip install memecrypt```, and the binary runs smoothly, printing out what seems to be a python byte string.

Let's analyse this further. If we spam control c as the program is running, it gives us an error message about a KeyboardInterrupt, saying it's within a file owo.py. We can inspect further in classic reversing tools in ghidra, and find all sorts of python functions like `__Pyx_PyObject_GetAttrStr` or `__Pyx_PyObject_Call2Args`. This shows us it seems to be a python install zipped up with some python code/bytecode, or compiled cython. We decided to look into tools specialised in reversing things like this, and came across a program called REpdb which is part of the pyREtic library, made for reversing python that is put together in executable files like this as well as bytecode.

In order to use REpdb, we needed an inject point. That's where memecrypt comes in. REpdb has to be run by the process it's reversing - the easiest way to do this was to force the process to import malicious python code. We can accomplish this by editing our memecrypt.py install, or by creating a fake memecrypt.py file. I did the latter, tony did the former.
Here is my fake memecrypt.py file where meme_orig is my renamed real memecrypt install.
```python
import sys, os
sys.path.append(os.path.join(".", "pyREtic"))
from pyREtic import REpdb
REpdb.set_trace()
import meme_orig
meme_cipher = meme_orig.meme_cipher
```
I added those last two lines so that the program could use meme_cipher normally.
With this setup, running the binary drops us into a REpdb prompt to inspect the program.
What do we see? As we step through, we can see the ciphertext `eDxTP2RoekN4KkVXeDpQQyU+Sy5cPidXZSR6QGRaLktkSycrITpQS1xXem5cV3pvZTpFb2NXekRcNkstZSRub2U6RW9qJGZH`  being loaded into a meme_cipher object along with the key lmao. What does it decrypt to?
It decrypts to ```"from secrets import token_bytes as hush;print(hush())"```
A little research shows us that token_bytes generates some cryptographically secure random bytes. Since it prints the output of this, that seems to be what our byte string is. Tony also found this earlier through attaching tools like gdb into the process.

What's very interesting is that the program decrypts this, and seemingly executes it. This means that by tampering with our memecrypt install and changing things in the decrypt function, we can make it run whatever we want.
I did lots of tampering to reap maximum information.
In the meme cipher class, I added the following:
```python
def __setattr__(self,attr,value):
    print(attr,value)
    self.__dict__[attr] = value
```
as well as this to decrypt:
```python
global ttt
if ttt < 1:
    ttt += 1
    return "target_code"
```
 and ttt = 0 to the top of the file , and print statements to always print the ciphertext and key being decrypted as well as the decrypted result.
Such that on the first run of the decrypt function, it would just return our fake code. We can enumerate with this, calling globals() and similar things to look around the scope. We find lots and lots of functions. This includes ```flag, frag, rick_roll, grant, artemis, _, __, uwu_whats_this_nuzzles_rawr_xd```, and much more as well as meme cipher object "uwu" and the module webbrowser imported as communism.

I wrote a small script to call every function with a small delay.

```python
return "import time\nfor func in filter(lambda x: type(x) == type(owo), list(globals().keys)): print(func(),func);time.sleep(5)
```
Showing me the output of every function and it's respective function. 
We get a lot here. First of all, the flag function returns a fake flag, decrypting the ciphertext `K3swTVxHOGtyWVclZmd0OGYueUZ5RzJYXForP1wwdHJbR1dhVGcrPytndFFUPzhMW0dcdA==` with the key 1337_revese_engineering. 

Various youtube links like https://www.youtube.com/watch?v=h0oclM1Yw2A, https://youtu.be/h6DNdop6pD8 and https://www.youtube.com/watch?v=dQw4w9WgXcQ are decrypted with the key yt and then used in webbrowser. We can't find too much else useful with this code injection, but it allows us to get a handle on what exactly is happening in this program.

From here, we moved on to static analysis in the decompiled C code.

 There's a lot more unknown ciphertexts we can find in the strings of the binary, specifically small ones.
Wait a second...
```C
undefined  [16] __pyx_pw_3owo_1owo(void)

{
  long *plVar1;
  undefined8 in_RAX;
  
  plVar1 = __pyx_n_u_T0YqVGBGJzZiLXYp;
  *__pyx_n_u_apollo = *__pyx_n_u_apollo + 1;
  *plVar1 = *plVar1 + 1;
  _Py_NoneStruct._0_8_ = _Py_NoneStruct._0_8_ + 1;
  _Py_XDECREF();
  _Py_XDECREF(plVar1);
  return CONCAT88(in_RAX,0xa7e160);
}
```
here, in the function owo, one of the small ciphertexts, `T0YqVGBGJzZiLXYp`, is referenced. Right afterwards, so is the word `apollo`. Why don't we attempt to decrypt `T0YqVGBGJzZiLXYp` with `apollo`?

We do, and it decrypts to `lastfrag`.
Last frag implies fragments, fragments of some form of larger ciphertext or key. We decided this had to be on track, and looked for other frags.
```C
undefined  [16] __pyx_pw_3owo_45frag(void)

{
  long *plVar1;
  undefined8 in_RAX;
  
  plVar1 = __pyx_kp_u_QVZHZUEqOnM;
  *__pyx_n_u_rain = *__pyx_n_u_rain + 1;
  *plVar1 = *plVar1 + 1;
  _Py_NoneStruct._0_8_ = _Py_NoneStruct._0_8_ + 1;
  _Py_XDECREF();
  _Py_XDECREF(plVar1);
  return CONCAT88(in_RAX,0xa7e160);
}
```
here! the ciphertext `QVZHZUEqOnM=` is mentioned, and so is `rain`! This decrypts to `frag1`. Finally... 
```C
undefined  [16] __pyx_pw_3owo_31i3_tiling_wm(void)

{
  long *plVar1;
  undefined8 in_RAX;
  
  plVar1 = __pyx_kp_u_ZGBXYmRbfXU;
  *__pyx_n_u_champions = *__pyx_n_u_champions + 1;
  *plVar1 = *plVar1 + 1;
  _Py_NoneStruct._0_8_ = _Py_NoneStruct._0_8_ + 1;
  _Py_XDECREF();
  _Py_XDECREF(plVar1);
  return CONCAT88(in_RAX,0xa7e160);
}
```
the ciphertext `ZGBXYmRbfXU=` is mentioned along with the word champions, and this decrypts to frag2.
No more small ciphertexts remainded, and linus confirmed it for us - these were all the frags we needed. 
Key: `rain`, CT: `QVZHZUEqOnM=`, PT: frag1
Key: `champions`, CT: `ZGBXYmRbfXU=`, PT: frag2
Key: `apollo`, CT: `T0YqVGBGJzZiLXYp`, PT: lastfrag

From there, we tried to figure out how to put them together. Putting together the ciphertexts, the keys, the plaintexts, all sorts of combinations. We searched for larger ciphertexts that we hadn't cracked yet, and found
`b2o+LiRjVll0eHw8TXteVk1dVXdVYyZzJHlvOiQ+XnQ2Y3xmU3tvOm97XklTOlYxNmMkXg==`
`QnxZNFtibWxPWD9udF5tcjgmd1ZbPG1XJw==`
`Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZu`
and
`JUdMP2czQ3MuM1s0TkclbHlsZ20vRmZteXxMZC9sfnZDeWo1TkdIQVF5IkFTNiRxJT5PIlY7ZnAlPGo1Tm58cg==`

eventually, will was able to decrypt 
`JUdMP2czQ3MuM1s0TkclbHlsZ20vRmZteXxMZC9sfnZDeWo1TkdIQVF5IkFTNiRxJT5PIlY7ZnAlPGo1Tm58cg==` with the key frag1frag2frag3 to get the plaintext ractf{Thing5_Wh1ch_Ar3_Bey0nd_My_C0mpreh3nsi0n}, which wasn't actually the flag.

But, we were told it was incredibly close.

frag1frag2frag3 didnt make much sense, we only had frag1, frag2 and lastfrag. Woa came up with the idea to try encrypting our "fake" flag with the key frag1frag2lastfrag to see what it looked like, and what did we get?
`Xjk6Y1N3PDAsP35BYn1uPGJtVk9Wdz1DU1leV1M6bix5d344Wn1eV159bkhaVzx4eXdTbg==`
This is remarkably close to the ciphertext we found in the binary, `Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZu`


The fact the encryption of a close flag with the key frag1frag2lastfrag resembles a ciphertext we had already found must've meant something.

From there, we tried concatenating  `Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZu` (the binary's ciphertext) with a bunch of other ciphertexts and throwing it into our related-key-bruteforce-script created by Tony. Eventually, `Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZu` + `QnxZNFtibWxPWD9udF5tcjgmd1ZbPG1XJw==` was concatenated to create the larger ciphertext `Xjk6Y1N3PDBWdz0jNjlTOFp9bCJ5bWxPRFZuQnxZNFtibWxPWD9udF5tcjgmd1ZbPG1XJw==`,which decrypted with the key frag1frag2lastfrag to the real flag.


#### Flag:actf{Th1ngs_Th4t_I_Cann0t_Compr3hend}
