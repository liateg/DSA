class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
       
        """
        the = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in the:
                return [i, the[need]]
            the[n]=i

       

