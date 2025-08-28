class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1  # Initialize l and r pointers

        while l < r: # while l pointer hasn't passed right 

            mid = (l + r) // 2 # find mid pointer from left and right ones

            # If the middle element is greater than the rightmost element, then the minimum must be to the right of 'mid'
            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                # Otherwise, the minimum is at 'mid' or to the left of 'mid'
                r = mid

        # left pointer at end now points to the minimum element
        return nums[l]