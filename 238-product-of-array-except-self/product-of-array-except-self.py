class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[nums[0]]
        post=[]
        answer=[]
        temp=1
        temp2=1
        for i in range(1,len(nums)):
            temp*=nums[i-1]
            pre.append(temp)
            temp2*=nums[len(nums)-i]
            post.append(temp2)
        post[:]=post[::-1]
        answer.append(post[0])

        for i in range(1,len(nums)-1):
            answer.append(post[i]*pre[i])
        answer.append(pre[-1])

        return answer
