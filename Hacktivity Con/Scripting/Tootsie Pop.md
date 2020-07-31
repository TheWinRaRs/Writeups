# Tootsie Pop


Yeah, it's another one of those nested compression challenges. Inside of the zip is a gzip compressed file, which has a compressed file of a compressed file, etc. etc. etc.

Anyway, all of the archive types it uses are extractable using 7z e <filename>

So I just used a script to continuously extract the current archive and then remove it until it could not be extracted anymore. Then, you can simply cat the last file left to get the flag, flag{the_answer_is_1548_licks}

NOTE: My script was called popper.py, you'll have to replace popper.py in the script with whatever you call your script.


```python
import os
def getnext(cur):
    code = os.system(f"7z e {cur} >/dev/null")
    if code:
        print("Extraction error... quitting!")
        quit()
    files = os.listdir('.')
    files.remove(cur)
    files.remove("popper.py")
    print(files[0])
    os.system(f"rm {cur}")
    return files[0]
cur = "pop.zip"
while True:
    cur = getnext(cur)
```

#### Flag: flag{the_answer_is_1548_licks}
