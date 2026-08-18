class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        j=0
        c=0
        g.sort()
        s.sort()

        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                c+=1
                j+=1
                i+=1
            else:
                j+=1

            
        return c