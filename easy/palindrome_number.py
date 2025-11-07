# Given an integer x, return true if x is a palindrome, and false otherwise

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        if (x >= 0):
            x = str(x)
            z = x[::-1]
            if (x == z):
                return True
            else:
                return False