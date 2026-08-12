from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch = defaultdict(int)
        re = 0
        l = 0
        longest = 0
        mq = 0

        for r in range(len(s)):
            ch[s[r]] += 1

            mq=max(mq,ch[s[r]])

          

            while r-l+1-mq > k:
                ch[s[l]] -= 1

               

                l += 1

            longest = max(longest, r - l + 1)

        return longest