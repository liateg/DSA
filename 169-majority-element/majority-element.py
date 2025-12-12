class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frq={}
        res,mc=0,0
        for i in nums:
            frq[i]=1+frq.get(i,0)
            if frq[i]>mc:
                mc=frq[i]
                res=i
        return res




       

        