# Password 1

Quick explanation: Take top 46 lines, take bottom 46 lines, take everything after [. Then sort. The n flag treats the first part as multi digit numbers instead of single ascii bytes. Then cut out just the flag chars, and delete newlines

```
head out -n 46 | tail -n 43 | cut -d '[' -f 2 | sort -n | cut -d "'" -f2 | tr -d \\n
```
#### Flag: CYCTF{pu771ng_th3_ch@r@ct3r$_t0g3th3r_1337}
