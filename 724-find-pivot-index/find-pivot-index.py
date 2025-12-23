class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right,left=-1,-11
      
       
        for i in range(len(nums)):
            if i==0:
                left=0
                right=sum(nums[i+1:])
            elif i==len(nums)-1:
                right=0
                left=sum(nums[0:i])
            else:
                left=sum(nums[0:i])
                right=sum(nums[i+1:])
            if left==right:
                return i

        return -1
            
