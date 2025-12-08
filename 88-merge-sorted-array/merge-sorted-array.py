class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0   # pointer for nums1
        j = 0   # pointer for nums2
        newar = []

        # merge until one list is finished
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                newar.append(nums1[i])
                i += 1
            else:
                newar.append(nums2[j])
                j += 1

        # add leftovers from nums1 (only from the real part up to m)
        while i < m:
            newar.append(nums1[i])
            i += 1

        
        while j < n:
            newar.append(nums2[j])
            j += 1

        
        for k in range(m + n):
            nums1[k] = newar[k]
