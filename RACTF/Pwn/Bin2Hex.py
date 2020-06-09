'''
Converts a binary file into an intel hex file

'''

'''
Usage: Bin2Hex.py -b <path to binary file> -o <path to hex to be created>
'''


def ConstructRecord(recordType, address, data):

    record = []

    recordType = recordType & 0xFF
    address = (address >> 8) & 0xFF, address & 0xFF
    numBytes = len(data) & 0xFF
    
    record.append(numBytes)
    record += address
    record.append(recordType)
    record += data
    
    checksum = 0
    for byte in record:
        checksum += byte
    checksum &= 0xFF
    
    # Two's complement
    checksum = ~checksum + 1
    checksum &= 0xFF
    
    record.append(checksum)

    recordStr = ':'
    for byte in record:
        recordStr += '{:02X}'.format(byte)
    recordStr += '\n'
    
    return recordStr

def convertBinaryToHex(binaryPath, hexPath, ignoreErasedRecords = True):
    
    hexFile = open(hexPath, 'w')
    
    hexFile.write(ConstructRecord(0x04, 0x0000, (0x00, 0x00)))

    address = 0
    with open(binaryPath, 'rb') as binaryFile:
        byte = binaryFile.read(1)
        numBytes = 1
        data = []
        while byte != b'':
            
            byte = int.from_bytes(byte, byteorder='big') & 0xFF
            data.append(byte)
            
            if numBytes >= 32:
                for val in data:
                    if val != 0xFF or not ignoreErasedRecords:
                        hexFile.write(ConstructRecord(0x00, address, data))
                        break
                data = []
                numBytes = 0
                address += 32
                
            numBytes += 1
            
            byte = binaryFile.read(1)
        
    hexFile.write(ConstructRecord(0x01, 0x0000, []))
        
    hexFile.close()

from optparse import OptionParser

if __name__ == "__main__":
    
    parser = OptionParser(usage="usage: %prog -b <path to binary file> -o <path to hex to be created>")
    parser.add_option("-o", "--hexPath",
                                        action="store",
                                        dest="hexPath",
                                        default="",
                                        type="string",
                                        help="Path to the hex file to be generated")
    parser.add_option("-b", "--binaryPath",
                                        action="store", # optional because action defaults to "store"
                                        dest="binaryPath",
                                        type="string",
                                        default="",
                                        help="Path to the binary file",)
    (options, args) = parser.parse_args()
     
 
    binaryPath = options.binaryPath
    hexPath = options.hexPath

    if not binaryPath:
        binaryPath = input("Input path to binary file to process:")
        
    if not hexPath:
        hexPath = input("Input path to hex file to be generated:")

    convertBinaryToHex(binaryPath, hexPath)
    
    print("Done! Created hex file: {}".format(hexPath))
    
