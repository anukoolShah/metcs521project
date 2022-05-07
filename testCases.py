import unittest
from RunLength import RunLength

class TermProjectTestCases(unittest.TestCase):
    __object1 = RunLength("aaaaabb")
    __encodedValue = __object1.encode()
    __decodedValue = __object1.decode()
    
    def test_RL_decode(self):        
        self.assertEqual(self.__decodedValue,'aaaaabb')
        
    def test_RL_encode(self):
        self.assertEqual(self.__encodedValue,'a5b2')

if __name__ == '__main__':
    unittest.main()