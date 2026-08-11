class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s=0
        for i in range(k):
            max_s+=nums[i]

        prev=max_s

        for i in range(1,len(nums)-k+1):
            cur=prev-nums[i-1]+nums[i+k-1]
            max_s=max(max_s,cur)
            prev=cur
        return max_s/k
