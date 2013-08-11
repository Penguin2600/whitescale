from whitescale.whitescale import flenser
import unittest


class TestWhiteScale(unittest.TestCase):

    def setUp(self):
        self.chardata = ["b", "01100010"]

        self.stringdata = ["ponies!@!", "011100000110111101101110011010010110"
                                        "010101110011001000010100000000100001"]

        self.whitedata = ["0110100001100101011011000110110001101111",
                          "\0\n\n\t\0\n\0\0\0\n \t\0\n \t\0\n  ", "hello"]

        self.transcoder = flenser()

    def test_byte2char(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.byte2char(self.chardata[1])
        self.assertEqual(result, self.chardata[0])

    def test_char2byte(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.char2byte(self.chardata[0])
        self.assertEqual(result, self.chardata[1])

    def test_chars2bytes(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.chars2bytes(self.stringdata[0])
        self.assertEqual(result, self.stringdata[1])

    def test_bytes2chars(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.bytes2chars(self.stringdata[1])
        self.assertEqual(result, self.stringdata[0])

    def test_whites2bytes(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.whites2bytes(self.whitedata[1])
        self.assertEqual(result, self.whitedata[0])

    def test_bytes2whites(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.bytes2whites(self.whitedata[0])
        self.assertEqual(result, self.whitedata[1])

    def test_encode(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.encode(self.whitedata[2])
        self.assertEqual(result, self.whitedata[1])

    def test_decode(self):
        # make sure the shuffled sequence does not lose any elements
        result = self.transcoder.decode(self.whitedata[1])
        self.assertEqual(result, self.whitedata[2])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWhiteScale)
    unittest.TextTestRunner(verbosity=2).run(suite)
