class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=1
        if len(nums)==1 or len(nums) == 0:
            return len(nums)
        while r < len(nums):
            if nums[r]==nums[r-1]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
               
                r+=1
        nums[l+1:]=["-"]*(len(nums)-l+1)
        return l+1

       