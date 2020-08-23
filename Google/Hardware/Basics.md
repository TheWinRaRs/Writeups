# Basics
### Hardware - Easy
For this challenge, we are provided with a short Verilog program, and a C++ wrapper for it using the Verilator library. Verilog is a language that is used to describe hardware and abstract it into a program.
`check.sv`
```
module check(
    input clk,
    input [6:0] data,
    output wire open_safe
);

reg [6:0] memory [7:0];
reg [2:0] idx = 0;

wire [55:0] magic = {
    {memory[0], memory[5]},
    {memory[6], memory[2]},
    {memory[4], memory[3]},
    {memory[7], memory[1]}
};

wire [55:0] kittens = { magic[9:0],  magic[41:22], magic[21:10], magic[55:42] };
assign open_safe = kittens == 56'd3008192072309708;


always_ff @(posedge clk) begin
    memory[idx] <= data;
    idx <= idx + 5;
    for(int i = 0; i < 8; i = i+1) begin
      $write("%b ", memory[i]);
    end
end

endmodule
```
This was my first time using Verilog, so most of the challenge involved learning the syntax. The C++ wrapper program essentially reads in one character at a time, up to 100, then runs the open_safe routine and checks its result. I realized it was likely a password checker, with our input being transformed in some way to result (if correct) in a 56 bit decimal (`3008192072309708`). If it reached this, we are sent the flag. Here's my understanding of the verilog.
```
Create an array of 8 x 7 bit fields (named memory)
Define a 7 bit input 'data'
Define a 56 bit array 'magic'
Read in a single 7 bit character, place it at memory[idx], then increase idx by 5. As idx is is a 3 bit field, this results in an overflow that shuffles the input order
The contents of memory is then shuffled in a fairly simple fashion into magic
The 56 bit wire 'kittens' is defined and filled with data from magic in a non-linear order
```
I initially attempted to manually step back from the final expected bits, but my unfamiliarity with Verilog syntax and conventions led to a different result every time. At this point, I decided to invest time into installing Verilator, allowing me to build the binary for myself; which would be needed to check my flag. The largest advantage though was the ability to add debugging statements in.
```
    $display("magic : %b", magic);
    $display("kit : %b", kittens);
    $display("Goal: %b", 56'd3008192072309708);
```
Using this, I could see how my data was transformed. I sent test pieces of data, starting at `0b0000001`, and doing a binary shift left each iteration; this was to give me recognisable patterns to work from.

We were able to get the states of the memory, magic and kittens arrays after entering each character.

From here, we can just manually work out where all the bits are after getting a test case:

`dddfffffffgggggggccccccceeeeeeehhhhhhhddddaaaaaaabbbbbbb`

Then, we can use this on our compare string to get the binary we want:

`00110111 01001100 01101111 01011000 00100101 00101010 01011111 1111000 (converted to 8-bit)`

And then simply decode this to get the password `7LoX%*_x`, which we enter on the remote to get the flag!

#### Flag: `CTF{W4sTh4tASan1tyCh3ck?}`
