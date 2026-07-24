class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new=sorted(nums)
        res=[]
        for i in nums:
            res.append(new.index(i))
        return res
