import sys
sys.path.append('../src')
from  kabisat import Kabisat
import unittest

class Test(unittest.TestCase) :

    def testCharTrue(self) :
        self.assertEqual(Kabisat(2016), True)
        self.assertEqual(Kabisat(2000), True)

    def testCharFalse(self) :
        self.assertEqual(Kabisat(1900), False)
        self.assertEqual(Kabisat(2001), False)
    
    def testNumber(self) :
        self.assertFalse(Kabisat("2019"))

if __name__ == '__main__':
    unittest.main()
