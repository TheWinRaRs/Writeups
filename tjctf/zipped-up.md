# Zipped up

We start with a .zip file. When we unzip, we get a directory called 0. It contains one file, 1.tar.bz2

If we decompress this file, we get a directory called 1, which contains 1.txt and another compressed file. This repeats.

The text files seem to contain `tjctf{n0t_th3_fl4g}`, I took a guess that at some level in this recursive compression has a .txt file that yields the flag.

This is relatively simple. Every file is either .kz3, .tar.bz2, or .tar.gz. We can use file extensions to detect which type of file it is, and then decompress. Script below\(a bit bad, I'm aware\) I unzipped up to directory 1 manually because it's different to the rest.

```python
start = 1
import os
def unzip(filename):
  os.system(f"unzip {filename}")
def untar(filename):
  os.system(f"tar -zvjf {filename}")
def gunzip(filename):
  os.system(f"tar -zvxf {filename}")
cur = start
while True:
  files = os.listdir(str(cur))
  file = next(filter(lambda x: '.txt' not in x, files)) # Ignore this monstrosity
  file = os.path.join(str(cur),file)
  if 'kz3' in file:
    unzip(file)
  elif 'bz2' in file:
    untar(file)
  else:
     gunzip(file)
  file = next(filter(lambda x: '.txt' in x, files)) # Again, ignore this monstrosity
  os.system(f"cat {os.path.join(str(cur),file)} >> flags.txt") # Basically puts the text file into flags.txt
  os.system(f"rm -rf {cur}") # Remove at your own risk, just cleans up and makes sure not to blow up your VM
  cur += 1
```

After running the script you'll be left with a file flags.txt. Majorly, flags.txt contains a bunch of `ljctf{n0t_th3_fl4g}` but if you filter this out using `grep -v` the flag will be revealed to you.

