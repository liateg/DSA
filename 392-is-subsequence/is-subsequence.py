class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        r=0

        while l<len(s):
            if r==len(t):
                return False
            if t[r]==s[l]:
                l+=1
            r+=1

        return True

