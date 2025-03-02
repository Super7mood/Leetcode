import unittest
from fibonacciSub import lenLongestFibSubseq
class Test_Fibonacci_Sub(unittest.TestCase):
    
    def test_true(self):
        self.assertEqual(lenLongestFibSubseq([1,2,3,4,5,6,7,8]), 5)
        self.assertEqual(lenLongestFibSubseq([1,3,7,11,12,14,18], 3))
        self.assertEqual(lenLongestFibSubseq([1, 4, 6], 0))
    
    def test_false(self):
        self.assertFalse(lenLongestFibSubseq([1, 2, 4, 5, 6, 7, 8, 9]), 2)

if __name__ == "__main__":
    unittest.main()