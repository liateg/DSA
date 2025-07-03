class Solution:
    def __init__(self):
        self.word = "a"

    def kthCharacter(self, k: int) -> str:
        if len(self.word) >= k:
            return self.word[k - 1]
        self.word += ''.join('a' if ch == 'z' else chr(ord(ch)+1)
                             for ch in self.word)
        return self.kthCharacter(k)
