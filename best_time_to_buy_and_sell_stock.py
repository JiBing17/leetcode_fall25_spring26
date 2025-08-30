class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 # max overall profit found
        curr_profit = 0 # curr profit given we sold at the curr day 
        min_price = float('inf') # new min price seen (buy at that price)

        for price in prices: # for each day - get price of stock in that day 
            if min_price > price: # update smallest val we seen so far - when to buy stock
                min_price = price
            profit = price - min_price # compute profit - if we sell stock on that day given we bought stock on the min val day
            max_profit = max(max_profit, profit) # update max profit if applicable
        return max_profit # return the most we made overall