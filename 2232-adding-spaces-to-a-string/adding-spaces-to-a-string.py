class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        p=0
        for i in spaces:

            ans.append(s[p:i])
            
            p=i
        ans.append(s[p:])

        return ' '.join(ans)
