# The hare and the tortoise

The program reads the flag from a file called flag.txt, and prints it out one character at a time. But it always gets killed!
Looking at the c code included in the directory, only a few sections seem relevant
* The process forks
* The process checks if it is the original, if so enters 'hare mode', otherwise enters tortoise mode
* In hare mode the process waits a while and then kills itself
* In tortoise mode the process reads a file one char at a time
So if we kill the process in hare mode before it kills itself along with the process in tortoise mode, we will get the flag!
Open 2 ssh sessions, in one start the binary, and in the other run ps aux. Kill the process with the larger PID, check in the other window, and the flag will be printed!
#### Flag: forgot lol
