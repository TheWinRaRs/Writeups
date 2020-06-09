# Really Secret Algorithm

More of a rev really :/

Simple first step is to extract all the b85 encoded values as bytes. The ct and e are just b85 encoded, so we can store those for later use with rsactftool


P and Q on the other hand are treated differently. They are xored with a variable called 's' (state) using 'walrus operators'. The function can be expressed as:
```
append(s^i)
s=s^i
append(s^j)
s=s^j
```
The encrypted bytes of p and q are also interleaved throughout the value we receive. As XOR is commutative and s is XORed with the value we have just recovered, we can simply run the script again to recover the original values for p and q, making sure to use the recovered values of p and q bytes to update the state. 
We recover primes 
```
p=8935533316664982385690426241789463156779334270200983340957286950060861311077151464930402912151709770833375547368974424564809135614170092179811531622097999
and
q=11379478034699907676633030046472807804044882783405443091999142030427354686298593670992789218031609011985520050382686352162426667346054932520656108554445759
```
Plugging our data into RsaCtfTool yields:   
#### Flag: ractf{DoY0uLik3MyW4lrus35}
