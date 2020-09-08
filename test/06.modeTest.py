import sys
sys.path.append('../src')
from mode import Mode
import unittest

class Test(unittest.TestCase) :

    def testAssertEqual(self) :
        self.assertEqual(Mode([1,2,3,4,5,6,6,8,8,6,9]), 6)
        self.assertEqual(Mode([87.5, 88.5, 60.5, 90.5, 88.5]), 88.5)

    def testAssertIsNot(self) :
        self.assertIsNot(Mode([1,2,3,4,5,6,6,8,8,6,9]), 3)
        self.assertIsNot(Mode([87.5, 88.5, 60.5, 90.5, 88.5]), 87.5)

    def testTrimNotNone(self) :
        self.assertIsNotNone(Mode([1,2,3,4,5,6,6,8,8,6,9]))
if __name__ == '__main__':
    unittest.main()
