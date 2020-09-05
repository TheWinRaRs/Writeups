# PreDestination

Download the file, open it in Autopsy etc.

Now based on the brief, this challenge has something to do with timezones, and how malware has changed it to something.

So after doing some googling about where timezones are stored in windows filesystems.

I found a registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet` &lt; \(in the case of this challenge its ControlSet001\)\Control\TimeZoneInformation \(access through C:\Windows\system32\config\system\) which leads to the flag of.

## Flag: zh3r0{Cicada3301}

