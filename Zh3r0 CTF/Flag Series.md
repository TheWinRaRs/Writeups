### Prenote: As all of these challenges were similar, we decided to combine these under one page.

<hr>

## Flag 1


nmap all ports to see port 4994 is open, just nc to it to get flag


#### flag :zh3r0{pr05_d0_full_sc4n5} 


<hr>

## Flag 2

Going back to port 324 (ftp)


the flag is in .../.../.flag


#### flag: zh3r0{You_know_your_shit}


<hr>

## Flag 3


curling port 22 robots.txt gives you a string in base58, decode to get /clue3349203.txt, curl that to get a lot of jsfuck, decode that to get an employee id, and then use that on port 4994 to get the flag


#### flag: zh3r0{y0ur_b0nu5_i5_p4id}

<hr>

## Flag 4


if we scan port 324, we can see it is an ftp server, which allows anonymous login.


ls -a ing gives us a ... dir (wow thanks hq), and then cding into it and ls -a ing again gives us a .stayhidden file. reading this gives us another employee id, which we can use to login to port 4994 again.


#### flag: zh3r0{y0ur_s4l4ry_wa5_cr3dit3d}

<hr>

## Flag 5

nmap, see http port on port 22, curl it to get flag


#### zh3r0{shouldve_added_some_filter_here}

