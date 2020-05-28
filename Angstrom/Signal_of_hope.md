# Signal_of_hope

Open program in cutter and disassemble main
```
call    signal     ; sym.imp.signal ; void signal(int sig, void *func)
```
Looking at "linux 7 signal" - we see a load, so I bruteforced them all until one worked - found it was `SIGABRT`
This means that we need to kill the program , or abort it
Spinning it up on the shell, we have to do
```
sh -c 'echo $$; exec myCommand'
```
Which gives up the PID of the program and then runs it
Open up a new shell, and do
`"kill -6 PID"`  
Bam!  
#### actf{h0p3_c4nn0t_m3nd_th3_p41n_th4t_y0uv3_c4us3d_m3}
