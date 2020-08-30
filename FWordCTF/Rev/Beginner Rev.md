# Beginner Rev

As usual angr went brrr after I stopped being stupid and made it search for the success address, not output, which resulted in file errors.
```python
import angr
import claripy #the solver engine

proj = angr.Project("./welcome", auto_load_libs=False)
sym_arg_size = 0x10 #Length in Bytes because we will multiply with 8 later
inp = [claripy.BVS('flag_%d' % i, 8 ) for i in range(sym_arg_size)]
flag = claripy.Concat(*inp + [claripy.BVV(b'\n')])
state = proj.factory.full_init_state(args=["./welcome"], stdin=flag)
for byte in inp:
    state.solver.add(byte >= ord('0'))
    state.solver.add(byte <= ord('9'))

simgr = proj.factory.simulation_manager(state)
good = 0x400000 + 0x12b2
bad = [0x400000 + 0x1669, 0x400000 + 0x167b]

simgr.use_technique(angr.exploration_techniques.DFS())
simgr.explore(find=good)
found = simgr.found[0]
print(found.solver.eval(flag, cast_to=bytes))
```
```
The solved input is 1755121917194838
```

#### FLAG: FwordCTF{luhn!_wh4t_a_w31rd_n4m3}
