
# Beginner
### Reversing - Easy
So what I *think* you were meant to do is actually do rev. But that's boring and work and I wanted to try out Angr; so I did.
```py
import angr, claripy
target = angr.Project('a.out', auto_load_libs=False)
input_len = 15
inp = [claripy.BVS('flag_%d' %i, 8) for i in range(input_len)]
flag = claripy.Concat(*inp + [claripy.BVV(b'\n')])


desired = 0x0010111d
wrong = 0x00101100

st = target.factory.full_init_state(args=["./a.out"], stdin=flag)
for k in inp:
    st.solver.add(k < 0x7f)
    st.solver.add(k > 0x20)


sm = target.factory.simulation_manager(st)
sm.run()
y = []
for x in sm.deadended:
    if b"SUCCESS" in x.posix.dumps(1):
        y.append(x)

#grab the first ouptut
valid = y[0].posix.dumps(0)
print(valid)
```
5 seconds later we have the flag
```
WARNING | 2020-08-24 02:21:03,963 | cle.loader | The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
[ ... SNIP ... ]
b'CTF{S1MDf0rM3!}\n'
```

#### Flag: CTF{S1MDf0rM3!}

