# EmojASM

```
➡️🎞️👁️🎞️❔🗃️📦🔨✉️😃😂⚖️⏪📼🎁🔨➡️📼🦔🗃️❔🗃️📦🔨✉️😁😅🏷️👁️📼📤✉️😀😀🐰
```
Broken down into logic:  
Move forward on tape 1, read the value into reg A  
Compare reg A to 0 (read: have we reach end of indexes)  
Load reg A into reg X  
Load garbage address into reg A  
If compare earlier was true jump to garbage and die  
Else reset tape 0  
---JUMP BACK POINT---  
Load value from reg X back into reg A  
Step forward in T0  
Decrement reg A  
Compare reg A to 0 (read: are we at right char)  
Load reg A into reg X  
Load address of jump back point into A  
If earlier comparison not true (i.e not at the char yet) jump to jump back point  
Else (we are at the char) read T0 and output, jump back to start  

#### Flag: ractf{5huffl1n'}
