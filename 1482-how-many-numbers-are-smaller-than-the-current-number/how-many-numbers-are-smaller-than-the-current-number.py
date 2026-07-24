class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=sorted(nums)
        res = [new.index(i) for i in nums]
        
        return res
