class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        for i in range(len(nums)):
            if nums[i]!= '_' and nums.count(nums[i])>1 :
                for j in range(1,nums.count(nums[i])):
                    nums.remove(nums[i])
                    nums.append('_')
                
            

        return len(nums)-nums.count('_')