# Penguins

we see a `.git` directory, so we navigate to it, and check out the objects we can decompress all the zlib files with

```python
for f in */*; do python -c "import zlib; print zlib.decompress(open('$f').read());";
```

one of them has a weird looking string in it: `blob 149YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9` removing the blob number gets us a b64decodable string, which gets us the flag:

## rgbctf{d4ngl1ng\_c0mm17s\_4r3\_uNf0r7un473}

