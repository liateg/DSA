class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        r = 0

        for i in range(len(tickets)):
            if i <= k:
                r += min(tickets[i], t)
            else:
                r += min(tickets[i], t - 1)

        return r