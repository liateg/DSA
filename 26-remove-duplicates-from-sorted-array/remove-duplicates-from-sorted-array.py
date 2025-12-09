class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nr=[nums[0]]
        c=0
        for i in nums:
            c=0
            for j in range(len(nr)):
                if i == nr[j]:
                    c+=1
            if c==0:
                nr.append(i)
        nums[:]=nr + ['_'] * (len(nums)-len(nr))
        return len(nr)