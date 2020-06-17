# UnRemovable
Anyway, continuing on from the previous one. 

This one has something to do with unremovable malware. So like, it also said that restarting the computer doesn't remove it so I googled startup tasks and where in a registry this would be. 

The registry is `SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\`. And if you go into `SpecialAccounts\Shell` you find the malware file that starts up.

####Flag: zh3r0{zh3r0ctfmalware.exe}
