class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m=[]

        i=0
        j=0
        while i<len(word1) and j<len(word2):
            if word1[i:] > word2[j:]:
                m.append(word1[i])
                i+=1
            else:
                m.append(word2[j])
                j+=1
        if i<len(word1):
            m.append(word1[i:])
        elif j<len(word2):
            m.append(word2[j:])

        return ''.join(m)
        