class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        clen=s.strip().split()
        return len(clen[-1])
