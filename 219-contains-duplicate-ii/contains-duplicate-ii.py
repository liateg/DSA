class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s={}
        for i,v in enumerate(nums):
            if v in s and i-s[v]<=k:
                return True
            else:
                s[v]=i
        return False
        