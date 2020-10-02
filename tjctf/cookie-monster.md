# Cookie Monster

Windows 7 sp1 x64 memdump By grepping for urls, we can find [https://super-secret-file-server.herokuapp.com/](https://super-secret-file-server.herokuapp.com/).
Command history shows us the credentials with a username and password, and also the name of a deleted file.
We download this file: \_4nd\_y0u\_w1ll\_n3v3r\_f1nd\_m333} 
We now see that mstsc is running, which is the rdp client.
I used filescan to search for open files, and found an the rdp cache file.
We can use [https://github.com/ANSSI-FR/bmc-tools](https://github.com/ANSSI-FR/bmc-tools) to parse it, and get 128 tiles from the image.
By piecing this together \(thanks will\) we get the first half of the flag: tjctf{c00k1e\_m0n5t3r\_w4s\_h3r3

## Flag: tjctf{c00k1e\_m0n5t3r\_w4s\_h3r3\_4nd\_y0u\_w1ll\_n3v3r\_f1nd\_m333}

