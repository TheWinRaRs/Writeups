# Tux Fanpage

There are two checks made to the page parameter:

1. If the first char is not alphanumeric, remove it, and keep removing until an alphanumeric char is found

2. If the string "../" (and basically all variants, url encoding etc.) are present, replace them with nothing, and keep replacing until none are left.

We can bypass this by having a decoy path parameter as something random (as long as its not an actual dir i think its fine), and then having an "&&path=" to add another path variable, which is unfiltered.

Therefore, our final payload becomes:

`https://tux-fanpage.2020.redpwnc.tf/page?path=a&&path=/../../index.js`

which gets us our flag!

#### Flag: flag{tr4v3rsal_Tim3}
