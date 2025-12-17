class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j=nums[0]
        i=0
        if len(nums)==1:
            return True
        while i<(len(nums)-1):
            if (len(nums)-1-(j+i))<=0:
                return True
            if j==0:
                return False
            j=max((j-1),nums[i+1])
            i+=1
        return False






      
