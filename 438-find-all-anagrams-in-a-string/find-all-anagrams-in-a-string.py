from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        wi=Counter(p)
        prv=Counter(s[:len(p)])
        ans=[]

        for i in range(len(s)-len(p)):
           
            if prv==wi:
                ans.append(i)
            prv[s[i]]-=1
            prv[s[i+len(p)]]+=1
        

        if prv==wi:
            ans.append(len(s)-len(p))
        
            
        return ans

