import sys
sys.path.append('../src')
from  rating import Rating
import unittest

class Test(unittest.TestCase) :

    def testAssertEqual(self) :
        self.assertEqual(Rating(21), 'DEWASA')
        self.assertEqual(Rating(13), 'REMAJA')
        self.assertEqual(Rating(9), 'BIMBINGAN ORANG TUA')
        self.assertEqual(Rating(8), 'SEMUA USIA')

    def testNotAssertEqual(self) :
        self.assertNotEqual(Rating(21), 'SEMUA USIA')

    def testNumber(self) :
        self.assertFalse(Rating("8"), False)


if __name__ == '__main__':
    unittest.main()
