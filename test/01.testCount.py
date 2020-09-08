import sys
sys.path.append('../src')
from  count import countChar
import unittest

class Test(unittest.TestCase) :

    def testAssertEqual(self) :
        self.assertEqual(countChar('abror'), 5)
        self.assertEqual(countChar('lari pagi'), 9)
        self.assertEqual(countChar('lari siang'), 10)

    def testAssertNotEqual(self) :
        self.assertNotEqual(countChar('abror'), 10)
        self.assertNotEqual(countChar('lari pagi'), 5)
        self.assertNotEqual(countChar('lari siang'), 5)
    
    def testAssertFalse(self) :
        self.assertFalse(countChar(4))

if __name__ == '__main__':
    unittest.main()
