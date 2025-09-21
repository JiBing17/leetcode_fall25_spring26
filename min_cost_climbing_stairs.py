class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [float("inf") for i in range(len(cost) + 1)] # min cumulative cost to reach the ith step where n+1 step is the top 
        dp[0] = cost[0] # cost to reach step at index 0
        dp[1] = cost[1] # cost to reach step at index 1 

        for i in range(2,len(cost) + 1): # populate the rest based off of the prev 2 steps cost + curr step cost 
            if i != len(cost): # case if not the top step  
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i] # min cost of the last 2 steps + cost of curr step is cumulative cost
            else: # computing top step
                dp[i] = min(dp[i-1], dp[i-2]) # no curr step cost so just min between the last 2 steps

        return dp[len(cost)] # return min cumulative cost to get to the top step