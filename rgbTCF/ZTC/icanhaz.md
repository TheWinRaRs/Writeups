# icanhaz

The file is a raw hexdump. De-hexdump-ing this and checking the filetype in cyberchef shows it is an xz compressed file.

Using an online tool, [https://extract.me/](https://extract.me/), you can extract a file from it.

This gives us the HTML for an SVG.

This SVG will form a QR code, but it's much easier to notice by replacing the ``#fffff6` colour with ``#000000 using` find and replace.

Scanning this QR code gives some base64 encoded data. Decompress this, and you get another xz file. Extracting this gives an ASCII art for a QR code - in inverted colours. Swap the colours and scan for the flag.

#### flag: rgbCTF{iCanHaz4N6DEVJOB}
