class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nr=[]
       
        for i in range(len(nums)):
            if val != nums[i]:
                nr.append(nums[i])
               
      
        nums[:] = nr + ['_'] * (len(nums) - len(nr))

        return len(nr)
            

