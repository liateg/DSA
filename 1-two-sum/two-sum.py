class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
       
        """
        diff={}
        for i in range(len(nums)):
            diff[i]=target-nums[i]
        for i in diff.keys():
            if diff[i] in nums and i!=nums.index(diff[i]):
                return [i,nums.index(diff[i])]

       

