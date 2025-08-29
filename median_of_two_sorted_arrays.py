class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        for num in nums1: # make one big array by adding all elements in nums1 to nums2
            nums2.append(num)

        nums2.sort() # sort in ascending order

        if len(nums2) % 2 != 0: # if odd size, return middle value - the median in this case
            return nums2[len(nums2) // 2]
        else:
            return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2 # if even add the two middle values and divide by 2