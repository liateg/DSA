class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a=0
        b=0
        while a<len(nums1) and b<len(nums2):
            if nums1[a]==nums2[b]:
                return nums1[a]
            elif nums1[a]>nums2[b]:
                b+=1
            else:
                a+=1

        return -1