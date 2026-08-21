class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        for i in range(len(s)):
            word=list(s[i])
            l=0
            r=len(word)-1

            while l<r:
                word[l],word[r]=word[r],word[l]
                r-=1
                l+=1
            s[i]=''.join(word)
        return ' '.join(s)
            