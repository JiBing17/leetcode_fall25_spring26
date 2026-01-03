class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # dp way with memo
        # DFS given curr day and if it is possbile to buy 
        # save state in map to prevent same recursive call

        n = len(prices) # num of days
        memo = {} # memoization
        def dfs(i, can_buy): # DFS for all possbile paths
            if i >= n: # evaluated all days
                return 0
            
            if (i, can_buy) in memo: # already computed before
                return memo[(i, can_buy)]
             
            if can_buy: # if we can buy a stock that day
                buy = dfs(i+1, False) - prices[i] # try path where we buy
                skip = dfs(i+1, True) # try path where we choose NOT to buy 
                res = max(buy, skip) # take best 

            else: # otherwise we CANT buy because we have stock already
                sell = dfs(i+2, True) + prices[i] # we can sell and skip day after for cooldown
                skip = dfs(i+1, False) # or we can choose NOT to sell yet and hold 
                res = max(sell, skip) # take best of those 2 options

            memo[(i, can_buy)] = res # save optimal sol in map to prevent running same DFS
            return res # return res for this call stack

        return dfs(0, True) # run DFS on first day where we can buy if needed        


        # brute force - DFS to find all possbile ways we can buy and sell given prices

        # on day i, we can choose to either buy (if waited 1 day) or sell (if we bought before) or skip and hold
        # return profit once we exhausted our options
        
        n = len(prices)
        def dfs(i, have_stock, cooldown):
            if i == n:
                return 0

            # Option 1: do nothing
            res = dfs(i + 1, have_stock, False)

            if have_stock:
                # Option 2: sell
                res = max(res, prices[i] + dfs(i + 1, False, True))
            else:
                if not cooldown:
                    # Option 3: buy
                    res = max(res, -prices[i] + dfs(i + 1, True, False))

            return res

        return dfs(0, False, False)




