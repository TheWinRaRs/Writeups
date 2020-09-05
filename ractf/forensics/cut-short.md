# Cut Short

We get what appears to be a broken png file.

If we open it up in ghex, we can see a weird IEND chunk, which, after comparing it with another png, turns out to be not normal.

So, I just removed the chunk, and then using the fixed png as a guide, I patched the hex to reveal the image.

## Flag: ractf{1m4ge\_t4mp3r1ng\_ftw}

