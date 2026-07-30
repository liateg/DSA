class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold=0
        valid=0

        while valid<len(nums):
            if nums[valid]!=0:
                nums[valid],nums[hold]=nums[hold],nums[valid]
                hold+=1
            valid+=1
        return nums