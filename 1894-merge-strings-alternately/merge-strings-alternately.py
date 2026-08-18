class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=0
        
        s=[]

        while a<len(word1):
            if a>len(word2)-1:
                s.append(word1[a:])
                break
            s.append(word1[a])
            s.append(word2[a])
            a+=1
        if a<len(word2):
            s.append(word2[a:])
        return ''.join(s)

        
