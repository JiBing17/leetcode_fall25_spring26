class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums) # sum of input arr
        if total % 2 != 0: # can't partition equally if sum is odd 
            return False

        half = total // 2 # get half val to indicate what val each partition needs

        # dp arr to indicate if we can partition 2 subsets to equal the ith val
        dp = [False for i in range(half + 1)] 
        dp[0] = True # base case 

        for num in nums: # for each val in nums
            for i in range(half, num-1, -1): # try all nums from between half and curr num
            # we can ith val if we could've already or we could make ith 
            # val - curr num (adding curr num would make mean we can make ith val)
                dp[i] = dp[i] or dp[i - num] 
            
        return dp[half] # return if we could've chosen numbers in nums to make half or not