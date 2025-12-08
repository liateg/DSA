class Solution(object):
    def merge(self, nums1, m, nums2, n):
        f=n+m-1
        n1=n-1
        m1=m-1
        while n1>=0 and m1>=0 and f>=0:
            if nums2[n1]>=nums1[m1]:
                nums1[f]=nums2[n1]
                f-=1
                n1-=1
            else:
                nums1[f]=nums1[m1]
                f-=1
                m1-=1
        if n1>=0:
            nums1[0:f+1]=nums2[0:n1+1]
        return nums1

       