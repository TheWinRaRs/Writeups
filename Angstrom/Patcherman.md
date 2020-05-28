# Patcherman

Look in hex - `line 01050` - `be ba 0d f0`
That spelled backwards is `f00dbabe`
Open cutter, go to graph, main
`'cmp eax, 0x1337beef'`
Convert that to the format it needs
```
python -c "import pwn; print(pwn.p32(0x1337beef))"  | hd - ef be 37 13
```
Swap that with `f00dbabe`
`./patcherman`
#### actf{p4tch3rm4n_15_n0_m0r3}
