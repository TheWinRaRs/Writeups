# P*rn Protocol
We're given a description of the protocol used to connect to the server. There's no exploitation, it's just understanding and inferring. Not much to writeup here really, so here's my script:
```py
from pwn import *
import struct
import uuid

r = remote("flu.xxx", 2005)

TYPES = {"MSG_ID": 0x1, "IDENT": 0x2, "MEM_ID": 0x3, "LGN": 0x4, "FLG": 0x5, "ERR": 0xFF}
ERRORS = {0x1: "TOO MANY", 0x2: "TOO SMALL", 0x3: "LENGTH MISMATCH", 0x4: "UNKNOWN TYPE", 0x5: "TOO FEW PAYLOADS", 0x6: "INCORRECT START", 0x21: "INVALID IDENT", 0x50: "NO FLAG"}
class Packet:
    def __init__(self, mType, mData):
        self.mType = mType
        self.mData = mData
        data = chr(len(mData) + 1).encode()
        data += chr(mType).encode()
        data += mData
        self.data = data
    def __repr__(self):
        mTypeS = str(self.mType)
        for k,v in TYPES.items():
            if v == self.mType:
                mTypeS = k
                break
        out = f"<Packet {mTypeS}, Length {len(self.mData) + 1}, "
        if self.mType == TYPES["ERR"]:
            out += f"Error {ERRORS[ord(self.mData)]}"
        else:
            out += f"Data {self.mData}"
        return out +  " >"

def m_id(messageId):
    p = Packet(TYPES["MSG_ID"], chr(messageId).encode())
    return p.data

def ident(identifier):
    p = Packet(TYPES["IDENT"], identifier)
    return p.data

def new_member():
    p = Packet(TYPES["MEM_ID"], chr(2).encode())
    return p.data

def get_flag():
    p = Packet(TYPES["FLG"], chr(1).encode())
    return p.data

def login(username, password):
    data = chr(1).encode() + chr(3).encode() + username + chr(4).encode() + password
    p = Packet(TYPES["LGN"], chr(1).encode())
    return p.data

def decode_packets(payload):
    out = []
    while len(payload) > 0:
        a, b = decode(payload)
        payload = payload[b:]
        out.append(a)
    return out


def decode(packet):
    length = packet[0]
    pType = packet[1]
    for k,v in TYPES.items():
        if v == int(pType):
            pTypeS = k
            break
    data = packet[2:1+length]
    return (Packet(pType, data), 1+length)



out = r.recv()
print(f"client <{'='*10} {out}")
for p in decode_packets(out):
    if p.mType == TYPES["IDENT"]:
        myid = p.mData
    print(p)
print("\n")
packet = m_id(0)
packet += ident(myid)
packet += new_member()
for p in decode_packets(packet):
    print(p)
r.send(packet)
print(f"{packet} {'='*10}> server")

out = r.recv()
print(f"client <{'='*10} {out}")
for p in decode_packets(out):
    if p.mType == TYPES["MEM_ID"]:
        if p.mData[0] == 3:
            username = p.mData[1:]
        elif p.mData[0] == 4:
            password = p.mData[1:]
    print(p)
print("\n")
print(f"Username: {username}, Password: {password}")


packet = m_id(1)
packet += ident(myid)
packet += login(username, password)
for p in decode_packets(packet):
    print(p)
print("\n")
print(f"{packet} {'='*10}> server")
r.send(packet)

out = r.recv()
if out == b'Username: ':
    print("Sending username")
    r.sendline(username)
else:
    exit()
out = r.recv()
if out != b'Password: ':
    exit()
print("Sending password")
r.sendline(password)
out = r.recv()
print(out)

packet = m_id(2)
packet += ident(myid)
packet += get_flag()
for p in decode_packets(packet):
    print(p)
print("\n")
print(f"{packet} {'='*10}> server")
r.send(packet)

out = r.recv()
for p in decode_packets(out):
    print(p)
print("\n")
```
#### Flag:flag{vpns_ar3_n0t_h4ck3r_appr0v3d}
