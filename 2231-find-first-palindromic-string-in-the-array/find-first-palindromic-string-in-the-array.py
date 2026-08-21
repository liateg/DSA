class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l=0
            r=len(i)-1
            c=0

            while l<=r:
                if i[r]!=i[l]:
                    c=0
                    break
                l+=1
                r-=1
                c=1
            if c:
                return i

        return ""
