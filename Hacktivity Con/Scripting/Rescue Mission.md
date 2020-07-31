# Rescue Mission

Idk how this is scripting? We get a powershell shell.

`gci -r` shows us the path of flag.png

`[Convert]::ToBase64String([IO.File]::ReadAllBytes("/c_drive/stuck_in/the_ocean/flag.png"))`

Just load that into cyberchef, decode, and render image

#### Flag:flag{thanks_you_saved_me}
