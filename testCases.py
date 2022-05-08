import unittest
from RunLength import RunLength
from Huffman import Huffman

class TermProjectTestCases(unittest.TestCase):
    __object1 = RunLength("aaaaabb")
    __encodedValue = __object1.encode()
    __decodedValue = __object1.decode()
    __object2 = Huffman("aaan")
    __HFencodedValue = __object2.encode()
    __HFdecodedValue = __object2.decode()
    
    def test_RL_decode(self):        
        self.assertEqual(self.__decodedValue,'aaaaabb')
        
    def test_RL_encode(self):
        self.assertEqual(self.__encodedValue,'a5b2')
        
    def test_HF_decode(self):        
        self.assertEqual(self.__HFdecodedValue,'aaan')
        
    def test_HF_encode(self):
        self.assertEqual(self.__HFencodedValue,'0001')

if __name__ == '__main__':
    unittest.main()