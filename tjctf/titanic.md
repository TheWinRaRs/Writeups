# Titanic

The first step is to get a list of all the words from the titanic:

```bash
curl http://www.dailyscript.com/scripts/Titanic.txt | tr '[:space:]' '\n' | sed  '/^$/d' | | tr -d '.' | tr -d ',' | tr '[:upper:]' '[:lower:]' > wl
```

Now we create a new wordlist in flag format:

```bash
for i in $(cat wl); do echo "tjctf{$i}" >> wl2; done
```

Then we can use the password cracking tool john to get the flag.

```bash
john -w=wl3 hash --format=raw-md5
```

## The flag is tjctf{ismay's}

