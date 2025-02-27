import unittest
from maxAbs import maxAbsoluteSum

class Test_Max_Abs(unittest.TestCase):

    def test_combinations(self):
        
        self.assertEqual(maxAbsoluteSum([1, 2, 3, 4]), 10)

        self.assertEqual(maxAbsoluteSum([1, 2, 3]), 6)

        self.assertEqual(maxAbsoluteSum([-1, -2, -10, 1]), 13)

        self.assertEqual(maxAbsoluteSum([1, 2, 3, -70]), 70)

        self.assertEqual(maxAbsoluteSum([1, 2, 3, -70, 5, -6]), 71)

        self.assertNotEqual(maxAbsoluteSum([-1, -2, 1, 4]), 8)

if __name__ == "__main__":
    unittest.main()