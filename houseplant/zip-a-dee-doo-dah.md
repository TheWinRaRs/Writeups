# Zip-a-dee-doo-dah

Relatively simple. The file is a large nested compression - it's been gzipped, tarred and zipped hundreds of times. gzip and tar dont have passwords so any gz or tar file we come accross we can simply decompress. The zips however, do have passwords. Luckily, these passwords are on an 100 word wordlist, allowing for easy brute force.

I wrote a script, the script: uses magic bytes to find out whether the file is a zip, gzip or tar decompresses it accordingly, cracking the password with a wordlist if it's a zipfile go onto the next iteration

At the end, you'll be left with a file called 0, containing the flag.

## rtcp{z1pPeD\_4\_c0uPl3\_t00\_M4Ny\_t1m3s\_a1b8c687}

```python
import os, zipfile
wordlist = []
with open("/home/isaac/CTFs/houseplant/wordlist.txt", 'r') as f:
    data = f.read()
    wordlist = data.split('\n')
def gunzip(filename):
    if "gz" not in filename:
        os.system(f"mv {filename} {filename}.gz")
        filename = filename + ".gz"
    os.system(f"gunzip {filename}")
def tar(filename):
    os.system(f"tar -xvf {filename}")
    if len(os.listdir('.')) > 1:
        os.system(f"rm {filename}")
def zipcrack(filename):
    # More complicated. Must brute force password via the wordlist.
    tocrack = zipfile.ZipFile(filename)
    cracked = False
    for password in wordlist:
        pwd = password.encode()
        try:
            tocrack.extractall(pwd = pwd)
            cracked = True
            break
        except:
            pass
    if cracked:
        os.system(f"rm {filename}")
    else:
        raise Exception("Was not able to crack zip.")
zipheader = bytes([0x50, 0x4b, 0x03, 0x04])
gzipheader = bytes([0x1f,0x8b])
# Tar headers vary, but we know it's tar if it's not zip or gzip.
for _ in range(1816):
    ourfile = os.listdir('.')[0]
    # Find out whether it's gzip, tar or zip. Then open accordingly.
    with open(ourfile,'rb') as check:
        first = check.read(4)
        if first == zipheader:
            zipcrack(ourfile)
        elif first[:2] == gzipheader:
            gunzip(ourfile)
        else:
            tar(ourfile)
```

