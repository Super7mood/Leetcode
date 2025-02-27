import unittest
from palindrom import isPalindrome

# These are the test cases
class TestCalculations(unittest.TestCase):

    # Test the positive numbers instances
    def test_positive(self):
        self.assertTrue(isPalindrome(121))
        self.assertFalse(isPalindrome(1212))
        self.assertTrue(isPalindrome(1))
        self.assertFalse(isPalindrome(12))
        self.assertTrue(isPalindrome(123454321))
        self.assertTrue(isPalindrome(1234554321))
        self.assertFalse(isPalindrome(1234564321))
    
    # Test the negative numbers instances
    def test_negative(self):
        self.assertFalse(isPalindrome(-121))
        self.assertFalse(isPalindrome(-1212))
        self.assertFalse(isPalindrome(-1))
        self.assertFalse(isPalindrome(-12))
        self.assertFalse(isPalindrome(-123454321))
        self.assertFalse(isPalindrome(-1234554321))
        self.assertFalse(isPalindrome(-1234564321))


if __name__ == "__main__":
    unittest.main()