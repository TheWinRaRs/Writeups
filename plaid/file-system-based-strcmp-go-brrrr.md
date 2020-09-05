# File-system-based strcmp go brrrr

`tar -zxvf <long ass file name>` gets you strcmp.fat32 Mounting it gives you loads of errors, so you can't actually cd into any of them  
Googling the error gives us a tool of fsck. As it's a fat32 filesystem, we need to use `fsck.vfat`

```text
sudo fsck.vfat -l -v -a -t ./strcmp.fat32
```

This gives us a load of files, but most noticeable is that the flag starts with PCTF  
So if we run it again, and grep for "P/C/T/F" we again get a load of results. If we look through those, we notice

```text
P/C/T/F/P/P/C/T/F/{W/H/A/T/_/I/N/_/T/A/R/N/A/T/I/O/N/_/I/S/T/H/1/S_/F/I/L/E/S/Y/S}
```

That's not correct, but if we grep for that \(excluding the "}" at the end\) we find

```text
P/C/T/F/P/P/C/T/F/{W/H/A/T/_/I/N/_/T/A/R/N/A/T/I/O/N/_/I/S/T/H/1/S_/F/I/L/E/S/Y/S/T/E/M/!}/SPACE/1
```

## Flag: P/C/T/F/{WHAT\_IN\_TARNATION\_IS\_THIS\_FILESYSTEM!}

