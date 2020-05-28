# Adventure Revisited

Wacky ass challenge lmao

Right so the hint.7z file, when downloaded, isn't actually a 7z file. You can cat it and it's a base64. run base64 -d hint.7z > hint and you'll find it's an image, showing that there is a hidden eval command on the bot.

Running jst eval on the rtcp discord server tells us it can't be run in that guild. We can invite the bot to our own discord server and run the command.

JST eval gives us the ability to run python code on their server.

We can communicate data back to ourselves via a return statement.

The first thing we'll want to do is find some variables. Doing return globals() shows us there's a lot of global variables with a value that's just HIDDEN. Not useful. We can write a simple loop like so
```
JST eval
g = globals()
for key in g:
  if 'rtcp' in g[key]
    return g[key]
```
The output of this script is the string `rtcp{}`. Seems like we're getting somewhere.

Remember: globals gives us variable names and their declared global value. What if instead of printing rtcp{}, we printed the key(variable name), and referenced that?

New script:
```
JST eval
g = globals()
for key in globals:
  if 'rtcp' in g[key]:
    return key
```
Giving us the variable name `fadlgncrjykmbw`

Therefore, we can do
```
JST eval
return fadlgncrjykmbw
```
To return the value at that variable.  
BOOM! Flag acquired.  
#### Flag: rtcp{1tz_n0t_4_bUg_1ts_a_fe4tur3}
