class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans=0
        piles.sort()

        for i in range(int(len(piles)/3),len(piles),2):
            ans+=piles[i]

        return ans
