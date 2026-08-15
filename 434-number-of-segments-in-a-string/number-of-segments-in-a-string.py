class Solution:
    def countSegments(self, s: str) -> int:
        if len(s):
            return len(s.strip().split())
        else:
            return 0