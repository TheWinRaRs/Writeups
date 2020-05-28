# Just Rust

Have a bit of an experiment
The input is broken down into 4 chunks of 8
Imagine the output like a grid
The first character is converted to binary and written to the grid like a diagonal line, with the lsb at the top. For the next character the line is shifted to the right one, and so on until all characters in the chunk have been written. This repeats for the next 3 chunks, except instead of 1, the numbers 2, 4 and 8 are written instead
After the string is written 40 is added to all squares and it is converted to ascii. To solve, unconvert, subtract 40 and reverse the process
gg, beat woak  
#### actf{b1gg3r_4nd_b4dd3r_l4ngu4g3}
