# Pie Generator

Relatively simple: you get a submission box to type in a number. You must predict the random number the site will generate.

The page is pretty bare. There's a form that makes post requests, and it has two fields - one is the number that we submit, the other is the timestamp. As we post, a javascript function is called to change the timestamp to our current time. Wait... they probably use that as the seed!

If we can control the timestamp option on the form, we control the seed. If we control the seed, we control what random number comes next.

Editing the javascript function doesn't seem to work, so we'll fire up burp suite. The timestamp is sent as a post parameter as part of the form. Burp suite allows us to intercept the post request  as our browser makes it and edit it.

First of all, let's edit the timestamp to be 1 and see what happens. Funnily enough, the website tells us we were wrong and that the correct answer is 1. We can do this again,this time changing our guess to 1  
BOOM! Flag acquired.  
#### rtcp{w0w_sO_p53uD0}
