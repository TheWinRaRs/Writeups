# Finding Server Information

We are given the name of the source code file `app.py`, and we need to find a way to read it.

We already have access to the admin section of the site from the previous challenge.

We are given links to three available videos that we can watch.

These all follow the format `/watch/XXXX.mp4`.

We are told the name of the file we need to read is called `app.py`

So we can try `/watch/app.py`.

In the source code of the page, we can see:

`data:video/mp4;base64,ractf{qu3ry5tr1ng_m4n1pul4ti0n}`

## Flag: ractf{qu3ry5tr1ng\_m4n1pul4ti0n}

