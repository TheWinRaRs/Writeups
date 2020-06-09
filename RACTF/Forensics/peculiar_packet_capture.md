# Peculiar Packet Capture
## Stego/Forensics

We are given a PCAP of some WPA2 encrypted traffic, including a handshake. We run aircrack-ng + rockyou.txt against it to retrieve the key: nighthawk. We then add this to Wireshark's 802.11 protocol settings, and reload to  get the decrypted traffic. One things stands out, a HTTP 200. This has attached with it a PDF, containing the flag.

# `ractf{j4ck_ry4n}`
