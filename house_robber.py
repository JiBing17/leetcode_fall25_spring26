class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))] # init dp arr, max amount we can rob up to the ith house (inclusive)

        if len(nums) == 1: # max is just that 1 house
            return nums[0] 

        dp[0] = nums[0] # max is just that 1 house given that we only saw this one
        dp[1] = max(nums[0], nums[1]) # max between this and the one before if there is 2 houses we seen so far

        for i in range(2, len(nums)): # compute the rest of the dp arr

            # max of robbing this house + cumulative amount from 2 hourses back vs not robbing curr house where it 
            # would be cumulative cost from 1 house back
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 

        return dp[len(nums)-1] # return max cost attainable up until the nth house