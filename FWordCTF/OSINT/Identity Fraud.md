# Identity Fraud


The start of the challenge links you to a twitter (https://twitter.com/1337bloggs). This brings you to the person of Fred Bloggs.

After looking through the followers of 1337 bloggs, you get a twitter of a team called Eword, mentioned in the challenge description (https://twitter.com/EwordTeam).]
We also get a CTFtime page(https://ctftime.org/team/131587), however looking at this brings nothing of interest.

[this is where the guessing picks up]

Maybe there was something on the CTFtime page that they didn't want us to see. 

Using the wayback machine ( a group of archived internet pages), we find 2 archived pages.

Clicking on one of these archived pages leads us to here.

https://web.archive.org/web/20200826195056/https://ctftime.org/team/131587


We can see a pastebin link (https://pastebin.com/8bk9qLX1) that leads us to some clues.

```
Hi Fred,
 
You said that you are good in OSINT. So, you need to prove your skills to join Eword.
 
Your task:
Find the leader of Eword, then find the flag in one of his social media accounts.
 
Hint:
https://pastebin.com/PZvaSjA0
```

The most interesting thing here is the 2nd pastebin link, leading us to some base64.

This base64 can be converted here: (https://base64.guru/converter/decode/file) and is reconstructed to a jpg.


We get 3 pretty big clues here:

1. The social media platform he uses (instagram, due to the layout resembling an Instagram story)
2. The line "thanks to the advisor for recommending it for me". This advisor refers to Trip Advisor, a reviw site.
3. A picture of the hotel he was staying at.


After using google lens, we find out that our target is staying at "Hilton Podgorica Crna Gora" in Macedonia.


After staring at reviews for an hour, I was stuck, until will came in and gave me a s*nity check, realisng that the person who we needed to catch was right in front of us the whole time.


The man we are looking for was found, 
Wokaihwokomas Kustermann.

He had the username of "check my instagram" on trip advisor, so a simple sherlock search should do the trick.

```
kali@kali:~/sherlock$ python3 sherlock WokaihwokomasKustermann

[*] Checking username WokaihwokomasKustermann on:
(made shorter for s*nity)
[+] Instagram: https://www.instagram.com/WokaihwokomasKustermann
```
We found an instagram! 

After opening his profile picture fully, you get the flag of:


#### Flag: Eword{c0ngraAatulationZzZz_aNd_w3lCom3_to_Eword_Team_!}
