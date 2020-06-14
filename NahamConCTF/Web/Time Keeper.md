# Time Keeper

Using web.archive.org, we can see previous captures of a given site. 

`https://apporima.com/` has two captures, one on `9th May 2020`, and another on `18th April 2020`. 

Seeing as this challenge appears to be themed around going back in time, `18th April` seems far more interesting to us. 

There is a blog post in the April capture, missing from the most recent version which reads: "Today, I created my first CTF challenge. 

The flag can be found at forward slash flag dot txt." If we visit `https://apporima.com/flag.txt`, we get a 404 message, but putting the URL in `web.archive.org` shows a capture in April which will give us the flag.


#### Flag: JCTF{the_wayback_machine}
