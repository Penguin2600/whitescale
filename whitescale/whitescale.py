class flenser(object):
    """encodes and decodes data as whitespace"""
    def __init__(self):
        super(flenser, self).__init__()

        #map our whitespaces to bitpairs
        self.whites = {"00": "\t",
                       "01": "\0",
                       "10": "\n",
                       "11": " ",
                       }
        #invert whites dict to get bytes dict
        self.bytes = {v: k for k, v in self.whites.iteritems()}

    def char2byte(self, char):
        charval = ord(char)
        return ''.join('01'[(charval >> x) & 1] for x in xrange(7, -1, -1))

    def chars2bytes(self, chars):
        slist = [self.char2byte(char) for char in chars]
        return''.join(slist)

    def byte2char(self, byte):
        cval = int(byte, 2)
        return chr(cval)

    def bytes2chars(self, bytes):
        bytelist = [bytes[i:i+8] for i in range(0, len(bytes), 8)]
        asciistring = [self.byte2char(byte) for byte in bytelist]
        return''.join(asciistring)

    def whites2bytes(self, string):
        blist = [self.bytes[char] for char in string]
        return''.join(blist)

    def bytes2whites(self, bytes):
        bitpairs = [bytes[i:i+2] for i in range(0, len(bytes), 2)]
        whitestring = [self.whites[bitpair] for bitpair in bitpairs]
        return''.join(whitestring)

    def encode(self, data):
        encodeable = self.chars2bytes(data)
        return self.bytes2whites(encodeable)

    def decode(self, data):
        decodeable = self.whites2bytes(data)
        return self.bytes2chars(decodeable)
