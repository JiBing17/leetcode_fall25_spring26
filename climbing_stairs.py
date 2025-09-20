class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: # only 1 stair, only 1 way 
            return 1

        dp = [0 for i in range(n+1)] # init dp arr to store num of ways to climb to the ith stair
        dp[1] = 1 # 1 way to climb to stair 1
        dp[2] = 2 # 2 ways to climb to stair 2 

        for i in range(3, n+1): # compute the res based on prev computations
            dp[i] = dp[i-1] + dp[i-2] # could only gotten to ith step by stepping 1 or 2 steps below so take sum of those
        return dp[n] # return num ways to get to the nth step