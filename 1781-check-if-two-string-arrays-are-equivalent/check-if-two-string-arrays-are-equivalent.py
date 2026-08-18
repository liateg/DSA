class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w=''.join(word1)
        q=''.join(word2)

        return w==q