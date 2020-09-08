import sys
sys.path.append('../src')
from convert import Convert
import unittest

class Test(unittest.TestCase) :

    def testAssertEqual(self) :
        self.assertEqual(Convert(20), 'dua puluh ')
        self.assertEqual(Convert(10), 'sepuluh')
        self.assertEqual(Convert(5), 'lima')

    def testAssertNotEqual(self) :
        self.assertNotEqual(Convert(20), 'sepuluh')

    def testConvertNotNone(self) :
        self.assertIsNotNone(Convert(5))



if __name__ == '__main__':
    unittest.main()
