class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        xrev=x[::-1]
        if(x==xrev):
            return True
        return False