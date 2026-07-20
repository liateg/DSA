class Solution:
    def similarPairs(self, words: List[str]) -> int:
        

        count={}
        incom=[]

        for w in words:
            k=''.join(sorted(set(w)))
            count[k]=count.get(k,0)+1
        res=0
        for c in count.values():
            if c >=2:
                res+=c*(c-1)//2

    
        return res

