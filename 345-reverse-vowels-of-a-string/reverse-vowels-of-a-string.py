class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1

        vow=set(['a','e','i','o','u'])
        s=list(s)

        while r>l:
            if s[l].lower() in vow and s[r].lower() in vow:
                s[l],s[r]=s[r],s[l]

                l+=1
                r-=1
            elif s[l].lower() in vow:
                r-=1
            else:
                l+=1
        return ''.join(s)
