from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        ans = []

        p = 0

        while p < len(s):
            rev = {s[p]}
            l = c[s[p]]

            i = p + 1

            while i < p + l:
                if s[i] not in rev:
                    rev.add(s[i])
                    l += c[s[i]]
                i += 1

            ans.append(l)
            p += l

        return ans