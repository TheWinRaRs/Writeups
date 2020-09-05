# PI 1- Magic in the air

## PI 1: Magic in the air

Open the pcap, add data to the columns by clicking on the packet bytes and right click &gt; Apply to column where it it highlights. Remove the other columns then go to File &gt; Export Packet &gt; Dissections &gt; As CSV. Remove the odd data such as Value, the white space and the odd data parts. Remove the speech marks with 'sed -i 's/"//g' . Then run this script on it

```python
newmap = {
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "del",
43: "tab",
44: "space",
45: "-",
47: "[",
48: "]",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}

myKeys = open("<filtered out file>")
i = 1
for line in myKeys:
    bytesArray = bytearray.fromhex(line.strip())
    #print "Line Number: " + str(i)
    for byte in bytesArray:
        if byte != 0:
            keyVal = int(byte)

            if keyVal in newmap:
                #print "Value map : " + str(keyVal) + " - -> " + newmap[keyVal]
                print newmap[keyVal]
            else:
                print "No map found for this value: " + str(keyVal)

                #print format(byte, "02X")
                i+=1
```

The output will have the number.

## Flag: rgbCTF{+46736727859}

