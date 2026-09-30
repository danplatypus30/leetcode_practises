class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] < nums2[j]:
                # have nums1, but nums2 bigger, insert nums2
                nums1[k] = nums2[j]
                j -= 1
            elif i >= 0:
                # have nums1, nums1 equal or bigger, insert nums1
                nums1[k] = nums1[i]
                i -= 1
            else:
                # nums1 ran out, insert nums2
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # if nums2 ran out first, no action needed


            
