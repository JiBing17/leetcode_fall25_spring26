class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # rewrite the nums1 arr going backwards since the extra (m+n - m) elements on the right are 0s so rewriting from there is fine without needing to store what nums originally belong to where
        
        # time : O(n + m)
        # space : O(1)

        i = m - 1
        j = n - 1 
        curr_index = n+m - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[curr_index] = nums1[i]
                i -= 1
                curr_index -= 1
            else:
                nums1[curr_index] = nums2[j]
                j -= 1
                curr_index -= 1

        while i >= 0:
            nums1[curr_index] = nums1[i]
            i -= 1
            curr_index -= 1

        while j >= 0:
            nums1[curr_index] = nums2[j]
            j -= 1
            curr_index -= 1
        
        return nums1
                