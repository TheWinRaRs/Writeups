# Signal\_of\_hope

Open program in cutter and disassemble main

```text
call    signal     ; sym.imp.signal ; void signal(int sig, void *func)
```

Looking at "linux 7 signal" - we see a load, so I bruteforced them all until one worked - found it was `SIGABRT` This means that we need to kill the program , or abort it Spinning it up on the shell, we have to do

```text
sh -c 'echo $$; exec myCommand'
```

Which gives up the PID of the program and then runs it Open up a new shell, and do `"kill -6 PID"`  
Bam!

## actf{h0p3\_c4nn0t\_m3nd\_th3\_p41n\_th4t\_y0uv3\_c4us3d\_m3}

