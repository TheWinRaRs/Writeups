# Grab your Jisho

As the title suggested, I grabbed my Jisho \(jisho.org\) and pasted the first "word" in.

In the side panel I saw 20-8-5 for the stroke numbers, which I immidiately recognised as A1Z26 cipher for 'THE'.

The characters were encoded into kanji with an equivalent stroke number.

I continued manual decryption until I identified the plaintext as [http://www.gutenberg.org/files/45723/45723-h/45723-h.htm](http://www.gutenberg.org/files/45723/45723-h/45723-h.htm) .

At this point I wrote a quick script to match kanji to letters 1:1 in one paragraph, and use replace on the whole text.

This was much faster, and once I had decrypted 10 or so paragraphs like this grepping for `rgb` yielded the encrypted flag - `璧技丩忄鰏叒讞鸞鸚鱺鑱磒夢洶飳勊淩鼱殆鸝钁厵鬱`. However, some kanji had values above 26.

I struggled with this for a while before trying to just extend them on the ASCII table, which worked!

## Flag: rgbctf{~\|~yominikui~\|~} \(meaning: illegible\)

