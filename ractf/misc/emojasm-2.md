# Emojasm 2

```text
➡️📼👁️📼📦🔨   - Read T0 into A, store in X. 
➡️🎞️👁️🎞️       - Read T1 into A
🍴🔨📦⛏️      - AND A in place with X, store result in Y.
👁️🎞️          - Read T1 back into A
🎷🔨📦🔨      - OR A in place with X, store result in X
🦔🔨🦔⛏️      - DEC X, DEC Y
❔⛏️          - CMP Y 0
✉️😁😍🏷️       - JNE 1D (decrement phase - this makes a subtraction loop,   
                subtracting Y from X, and leaving result in X.)
🎁🔨📤        - Print X
➡️📼👁️📼⬅️📼    - Read the next char from T0 into A, move back.
❔🗃️          - CMP A 0 (is the tape empty)
✉️😀😀🏷️       - JNE 00
➡️🎞️👁️🎞️⬅️🎞️    - Read the next char from T1 into A, move back.
❔🗃          - CMP A 0 (same thing but makes sure both are empty
️✉️😀😀🏷️       - JNE 00
🗿            - HLT
```

This works because the difference between the AND of two numbers and the OR of those numbers, logically, is equal to the XOR. OR is also always greater than AND, as it has 1s in all the same places, and more.

## Flag: ractf{x0rmoj1!}

