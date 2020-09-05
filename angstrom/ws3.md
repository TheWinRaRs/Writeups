# WS3

* http.request.method == GET on wireshark
* Export Objects &gt; HTTP &gt; git-receive-pack
* Create a new git repo
* Place in the git repo
* Open in hex editor and fix the file header to be just 'PACK' at the beginning \(remove all the crap\)
* Now git unpack-objects &lt; git-receive-pack
* Navigate to objects folder, here there are 3 git objects:
  * a commit
  * a tree file
  * a blob file
* Decompress the zlib blob file with: python -c "import zlib; print zlib.decompress\(open\('3f47cbcb3ad8e946d0aad59259bdb1bc9e63f2'\).read\(\)\);" &gt; flag.jpg
* Open the file up in a hex editor and remove the first few bytes so the header is a jpeg header
* Open it up for the flag

  **actf{git\_good\_git\_wireshark-123323}**

