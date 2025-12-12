class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # frq={}
        # res,mc=0,0
        # for i in nums:
        #     frq[i]=1+frq.get(i,0)
        #     if frq[i]>mc:
        #         mc=frq[i]
        #         res=i
        # return res

        res=nums[0]
        c=0
        for i in nums:
            if c==0:
                res=i
            if res==i:
                c+=1
            else:
                c-=1
        return res
           




       

        