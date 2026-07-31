class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = m - 1
        b = n - 1
        k = m + n - 1

        while a >= 0 and b >= 0:
            if nums1[a] > nums2[b]:
                nums1[k] = nums1[a]
                a -= 1
            else:
                nums1[k] = nums2[b]
                b -= 1
            k -= 1

        while b >= 0:
            nums1[k] = nums2[b]
            b -= 1
            k -= 1