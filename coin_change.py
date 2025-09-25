class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)] # init dp arr - min coins to make i cent
        dp[0] = 0 # base case 0 coins to make 0 val

        for i in range(amount+1): # populate dp arr
            for coin in coins: # try every coin for curr val
                if i - coin >= 0: # if it can fit
                    # min coin for ith val is either curr min or this coin + min coin for the diff val
                    dp[i] = min(dp[i], dp[i-coin] + 1) 

        if dp[amount] != float('inf'): # if dp val changed from init val 
            return dp[amount] # return the min coins used to make amount  
        return -1 # otherwise we can't make amount with the given coins
