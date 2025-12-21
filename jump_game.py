class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if curr i position + nums[i] reaches last index, than we know reaching positoon i is same as reaching last index, 
        # so we set last index to i, continue until either last index becomes 0 (reachable from the start) 
        # or not in which it is not possible to reach that value 
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            jump = nums[i]

            if jump + i >= goal:
                goal = i 
        return goal == 0
