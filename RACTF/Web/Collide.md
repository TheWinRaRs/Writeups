# Collide

The server expects two values (`one` and `two`) passed in as a JSON array.

It appends a secret to the start of both of these and runs them through a custom hashing function. 

If the result is equal, we get the flag. However, our input is compared with the `===` operator, and if they match our input is rejected.

As this is a web challenge, not a crypto one, I realized the target was not the hashing function.

After some playing around, I found that `['a'] === ['a']` returns false, likely because the arrays are two different objects in memory.

We send to the server:
```json
{
	"one":["a"],
	"two":["a"]
}
```
and the flag is returned.

#### ractf{Y0u_R_ab0uT_2_h4Ck_t1Me__4re_u_sur3?}
