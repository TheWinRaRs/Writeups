# SmArT-Solver

We can tell the name is a clear reference to a SAT-solver. Running the program, it asks for a flag, then tells us whether it's correct or incorrect.

Opening it up in ghidra, we see a lot goes on. Specifically, it does A LOT of checks. It reads your input onto the stack, and does many checks against the characters. Every check is of the form

characterofinput < othercharacterofinput

If any of these checks are true, it tells us the flag is incorrect. If none of these are satisfied, it goes ahead and checks that all of the chars are alphanumeric. If not, it tells us the flag is incorrect. If all these checks pass, it tells us the flag is correct.

Clearly, the way to go here is to use a sat solver to figure out what possibilities fit all of the checks. I used the Z3 python API.

I ran some simple parses on the input to create a Solver object, and then extracted the model. Note: the chall desc says all letters are lowercase, and we know the flag regex, so this allows us to significantly reduce the range.

My full script is uploaded below.

For some reason, it thinks the last char is | not }, but that doesn't matter and is easily fixable.

#### Flag: flag{thequickbrownfoxjumpedoverthelazydogandlearnedhowtoautomateanalysis}
