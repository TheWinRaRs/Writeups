# Patchwork Quilt

We're provided with a download of the VScode source code, slightly modified. The name hinted at a patch happening, so I ran `git diff` and found a 'backdoor' leading to congonator.me/?id=ZmxhZ3tkb250X3RydXN0X2RvZGd5X2Rvd25sb2Fkc30%3D&key= when a key was pressed. I just decoded the `id` paramater, which revealed the flag.

## flag{dont\_trust\_dodgy\_downloads}

