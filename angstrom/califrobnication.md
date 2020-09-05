# Califrobnication

```text
./califrobnication > ~/file & echo $! | date on shell server
```

This will give you an exact timestamp and an approximate PID Next run following command locally, with a flag.txt file of length 49

```bash
date +%s -s @<UNIX TIMESTAMP HERE> ;sudo echo <PID-2 HERE> > /proc/sys/kernel/ns_last_pid; ./califrobnication | hd
```

You will get a number of different outputs  
Look for one that has the last letter of flag.txt xor'ed in the same place as the } xor'ed was on the shell  
Dexor  
Reassemble the flag  
GG;No re

## actf{dream\_of\_califrobnication\_1f6d458091cad25}

