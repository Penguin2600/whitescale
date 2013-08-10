class flenser(object):
    """encodes and decodes data as whitespace"""
    def __init__(self):
        super(flenser, self).__init__()
        self.whites = {"00": "\t",
                       "01": "\r",
                       "10": "\n",
                       "11": " ",
                       }
        self.bytes = {"\t": "00",
                      "\r": "01",
                      "\n": "10",
                      " ": "11",
                      }

    def byte2char(self, byteStr):
        chrVal = 0
        bitPos = 8
        for bit in byteStr:
            bitPos -= 1
            if bit == "1":
                chrVal += (2**bitPos)
        return chr(chrVal)

    def char2byte(self, char):
        charval = ord(char)
        return ''.join('01'[(charval >> x) & 1] for x in xrange(7, -1, -1))

    def string2bytes(self, string):
        slist = [self.char2byte(letter) for letter in string]
        return''.join(slist)

    def whites2bytes(self, string):
        blist = [self.bytes[letter] for letter in string]
        return''.join(blist)

    def bytes2whites(self, string):
        bitposition = 0
        bytestring = ""
        whitestring = ""
        for bit in string:
            bytestring += (bit)
            bitposition += 1

            if bitposition == 2:
                bitposition = 0
                whitestring += self.whites[bytestring]
                bytestring = ""
        return whitestring

    def bytestring2ascii(self, string):
        bitposition = 0
        bytestring = ""
        asciistring = ""
        for bit in string:
            bytestring += (bit)
            bitposition += 1

            if bitposition == 8:
                bitposition = 0
                asciistring += self.byte2char(bytestring)
                bytestring = ""
        return asciistring

    def encode(self, data):
        encodeable = self.string2bytes(data)
        return self.bytes2whites(encodeable)

    def decode(self, data):
        decodeable = self.whites2bytes(data)
        return self.bytestring2ascii(decodeable)
