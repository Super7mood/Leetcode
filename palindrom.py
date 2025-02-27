# This funciton checks if the numbers are palindroms or not
def isPalindrome(x: int):
        
        # Checks if the number is negative
        if x < 0:
            return False # Returning false for negative numbers since negative number have the negative "-" symbol hence they can't be a palindroms
        
        numList = [] # Stores the list of number in the iteger

        # Iterate throgh the number and stores values in the list
        while x != 0:
            numList.append(abs(x) % 10) # Stores the last value of number in the list by getting the remainder
            x = int(x / 10) # Take out the number that was added to the list from x
        
        # Iterate through the list and checks if the first and last values are palindrom while removing them
        while len(numList) > 1:
            if numList.pop(0) != numList.pop(-1):
                return False
        
        return True # Return True as the list size is smaller than 2 hence it is a palindrom

import unittest

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
        self.assertTrue(isPalindrome(-121))
        self.assertFalse(isPalindrome(-1212))
        self.assertTrue(isPalindrome(-1))
        self.assertFalse(isPalindrome(-12))
        self.assertTrue(isPalindrome(-123454321))
        self.assertTrue(isPalindrome(-1234554321))
        self.assertFalse(isPalindrome(-1234564321))


if __name__ == "__main__":
    unittest.main()