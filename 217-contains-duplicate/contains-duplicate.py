class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        unique=set()
        for i in nums:
            unique.add(i)
        if len(unique)==len(nums):
            return False
        return True