# Good Ol' IE

This time though it wants you to find the origin of the malware that changed the time zone shid. 

Since the challenge had IE I had a feeling it had stuff to do with Internet Explorer and URL history. 

But looking through the most obvious files like the History folder had nothing sus. 

So I had to google like where applications are stored in a registry file (this is because I thought that malware was downloaded and I had to look for a file instead). 

I found that NTUSER.dat in the user's directory had this stuff in it. 

But looking through I found an Internet Explorer registry key and thought I'd try looking through that stuff again and to my surprise I found a flag in NTUSER.dat\Software\Microsoft\Internet Explorer\TypeURLs\url11. UwU OwO.

#### Flag: zh3r0{http://w3.you-got-million-dollars-click-me.nr.hg.org.tech/}
