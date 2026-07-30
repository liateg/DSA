class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        si=0
        ti=0
        for i in s:
            si+=ord(i)
        for i in t:
            ti+=ord(i)

        return chr(ti-si)
