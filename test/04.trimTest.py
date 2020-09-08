import sys
sys.path.append('../src')
from trim import Trim
import unittest

class Test(unittest.TestCase) :

    def testAssertEqual(self) :
        self.assertEqual(Trim("Ini adalah kalimat",5), 'Ini a...')
        self.assertEqual(Trim("Ini adalah kalimat",10), 'Ini adalah...')
        self.assertEqual(Trim("Ini adalah kalimat",15), 'Ini adalah kali...')

    def testTrimNone(self) :
        self.assertIsNotNone(Trim(None,2))

    def testTrimNotNone(self) :
        self.assertIsNotNone(Trim("Ini adalah kalimat",15))
    
if __name__ == '__main__':
    unittest.main()
