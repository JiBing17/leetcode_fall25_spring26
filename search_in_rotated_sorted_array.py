class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1 # define l and r pointers
        while l < r: # while r and l pointers have't passed each other
            mid = (l + r) // 2 # make mid pointer
            if nums[mid] > nums[r]: # if left half is normal, search right half for rotated origin
                l = mid + 1
            else: # if right half is normal, search left half
                r = mid # include mid in next left half since nums[mid] can == nums[r]

        start_val = l # index of origin val

        l,r = 0, len(nums) - 1

        if target >= nums[start_val] and target <= nums[r]: # define lower and upper bound given the origin value and target val
            l,r = start_val, r # search right half of origin val
        else:
            l,r = 0, start_val # search left half of origin val

        while l <= r: # basic binary search given the correct half to search

            mid = (l + r) // 2 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1 # cant find target, reutrn -1 at end