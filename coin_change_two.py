class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins) 

        # dp[i][j] = dp[i+1][j] + dp[i][j+coins[i]]
        # dp[i][j] = num ways to make amount given coins starting at i and curr amount being j

        dp = [[0 for i in range(amount+1 )] for j in range(n+1)] 

        for i in range(n+1): # if curr amount already == amount, then there is 1 way given ANY coins we start with
            dp[i][amount] = 1
        
        for i in range(n-1,-1,-1): # bottom up due to dp relationship dependencies
            for j in range(amount-1,-1,-1):

                use = 0 # ways to make amount if we use curr coin 
                skip = 0 # ways to make amount if we DONT use curr coin

                if i + 1 <= n:
                    skip = dp[i+1][j] # ways to make amount would depend on ways if we want to still make amount given j currently but we skip using curr coin (i+1) and stick with j as curr amount
                if i <= n and j + coins[i] <= amount: 
                    use = dp[i][j+coins[i]] # ways to make amount if we use curr coin, then we look at ways we could've made amount if the new amount (no i+1 since we can reuse)

                dp[i][j] = skip + use # add the two cases to find ways to make amount of curr j starting at coin i
        return dp[0][0] # return num ways to make amount starrting at coin 0 with curr amount being 0 



        def dfs(i, curr):
            if curr == amount:
                return 1
            if i >= n or curr > amount:
                return 0

            return dfs(i, curr + coins[i]) + dfs(i+1, curr)

        return dfs(0, 0)
    


    
    
            