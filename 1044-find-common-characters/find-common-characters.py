class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]

        for c in words[0]:
            ct=0
            for i in range(1,len(words)):
                if c not in set(words[i]):
                    break
                ct+=1
                words[i]=words[i].replace(c, "", 1)

            if ct==len(words[1:]):
                ans.append(c)

        return ans
