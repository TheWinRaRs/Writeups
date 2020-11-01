# Babyrev - Rev

The binary runs some byte by byte byte mangling, changing bytes based on their position, then compares it with some value. Could I rev this? Yes. Did I? No. I simply decompiled with ghidra, recompiled it to print the encrypted data instead of verifying, and fuzzed it.

This gets you the flag CYCTF{i_dueqq_aapia_qeu_uaq_qmm_ey_dlp_ymu}

Make sure that you put the plaintext CYCTF{ into the fuzzer first, otherwise you'll hit some random collisions

There's lots of possible flags, I ended up having to dm an admin to allow the flag I got to be submitted.

#### Flag: CYCTF{i_dueqq_aapia_qeu_uaq_qmm_ey_dlp_ymu}
```py
from pwn import *
target = '3E3?6]QHKTHQQBEETTNKZQ]K]?K<KHH<BQ<KQT<QHNT'
import string
alph = string.ascii_uppercase + '{}_!*@1234567890-=+?' + string.ascii_lowercase
#alph = bytes(range(256)).decode('latin-1')
known = 'CYCTF{'
for i in range(len(known),len(target)):
    for attempt in alph:
        totry = known + attempt
        p = process("./recomp")
        p.clean()
        p.sendline(totry)
        if p.recvline().decode('latin-1')[i] == target[i]:
            known += attempt
            print(known)
            p.close()
            break
        p.close()
    else:
        print("Bruteforce failed")

```
recomp.c:
```c
int main(){
    char cVar1;
  int iVar2;
  char local_48 [48];
  int local_18;
  int local_14;
  int local_10;
  char local_9;

  puts("Hello World");
  puts(
      "Welcome to the Flag checker program. Please enter your flag here, and we will verify whetherit is correct!"
      );
  __isoc99_scanf("%48s",local_48);
  local_9 = '\x01';
  local_10 = 0;
  while (local_10 < 0x2b) {
    if ((local_10 < 0) || (7 < local_10)) {
      if ((local_10 < 9) || (0xf < local_10)) {
        if ((local_10 < 0x11) || (0x18 < local_10)) {
          if ((local_10 < 0x17) || (0x22 < local_10)) {
            if ((0x25 < local_10) && (local_10 < 0x2c)) {
              local_48[local_10] = local_48[local_10] + -0xd;
            }
          }
          else {
            local_48[local_10] = local_48[local_10] + -0xd;
          }
        }
        else {
          local_48[local_10] = local_48[local_10] + '\a';
        }
      }
      else {
        local_48[local_10] = local_48[local_10] + -5;
      }
    }
    else {
      local_48[local_10] = local_48[local_10] + '\x03';
    }
    local_10 = local_10 + 1;
  }
  local_14 = 0;
  while (local_14 < 0x2b) {
    cVar1 = local_48[local_14];
    if (cVar1 < '\0') {
      cVar1 = cVar1 + '\x03';
    }
    local_48[local_14] = cVar1 >> 2;
    local_14 = local_14 + 1;
  }
  local_18 = 0;
  while (local_18 < 0x2b) {
    local_48[local_18] = local_48[local_18] * '\x03';
    local_18 = local_18 + 1;
  }
  puts(local_48);
}
```
