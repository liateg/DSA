class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        rev = {}
        for num, f in freq.items():
            rev.setdefault(f, []).append(num)

        res = []
        for f in sorted(rev, reverse=True):
            res.extend(rev[f])
            if len(res) >= k:
                return res[:k]