# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums) - 1 # define left and right pointers
        while l <= r: # keep going until l pointer passes right pointer (if equal we keep going since we are searching a num)
            mid = (l + r) // 2 # get mid pointer from left and right pointers
            val = nums[mid] # find value that mid pointer is pointing at
            if val == target: # found target return the index
                return mid
            elif val > target: # too big move right pointer left for smaller value for next mid pointers since sorted
                r -= 1
            else:
                l += 1 # same for too small case
        return -1 # out of while loop, no matches, return -1