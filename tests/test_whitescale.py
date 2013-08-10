import whitescale
import unittest

class TestWhiteScale(unittest.TestCase):

    def setUp(self):
        self.achar = "b"  #01100010
        self.bchar = "01110000"  #p
        self.asciidata = "ponies!@!"
        self.bindata = "01100100011001010111001001110000"  #derp
        self.transcoder = whitescale.flenser()

    def test_byte2char(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.byte2char(bchar)
        self.seq.sort()
        self.assertEqual(result, "p")

if __name__ == '__main__':
    unittest.main()
