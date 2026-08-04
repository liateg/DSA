class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        c=0
        nums.sort()

        while l<r:
            if nums[l]+nums[r]==k:
                c+=1
                r-=1
                l+=1
            elif nums[r]+nums[l]<k:
                l+=1
            else:
                r-=1
        return c
