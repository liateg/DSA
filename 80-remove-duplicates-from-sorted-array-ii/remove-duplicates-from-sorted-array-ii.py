class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        if len(nums)==0 or len(nums)==1 or len(nums)==2:
            return len(nums)
        l=1
        r=2
        temp=nums[l-1]
        while r<len(nums):
            if nums[r]==nums[r-1]==temp:
                r+=1
            else:
                
                l+=1
                temp=nums[l-1]
                nums[l]=nums[r]
                r+=1
        nums[l+1:]=['_']*(len(nums)-l+1)
        return l+1