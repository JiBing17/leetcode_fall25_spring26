class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # time: O(n^3)
        # space : O(n^2) 

        nums = [1] + nums + [1] # add boundaries for out of bounds slot coin values
        memo = {} # memoization to prevent calling same DFS with same state 

        def dfs(l,r):
            if l > r : # evaluated the entire arr  
                return 0 # return product if we have nothing to eval 
            
            if (l,r) in memo: # memoize to return early if computed already
                return memo[(l,r)]
            
            memo[(l,r)] = 0

            for i in range(l, r+1): # for loop for decision tree on which balloon we will end up popping last 
                coins = nums[l-1] * nums[i] * nums[r+1] # compute product as if it was popped last
                coins += dfs(l, i-1) + dfs(i+1, r) # add to product the subproblems to decide what balloons should be pop prev of that which would be sum of the two sub problems with their bounds adjusted as well
                memo[(l,r)] = max(memo[(l,r)], coins) # take the answer that will maximize our score and "remember it" 
            
            return memo[(l,r)]
        return dfs(1, len(nums) - 2) # run DFS where bounds start at the entire array

        # given n balloons each with a num that inddicates the num of coins inside balloon
        # if we pop a balloon we want the product of that and the adjacent balloons (not popping adjacent ones).
        # if no adjacent balloons, have dummy value of 1 instead
        # find the max amount of coins we can make by popping balloons in an optimal way

        # brute force way using DFS
        # find ALL possible ways we can pop ballons   

        # record index i to indicate which balloon we are looking at, have a visited set to indicate the indices that have already popped within this DFS path to tell us that we can't use that balloon as the adjacent ones or to pop it

        # pop balloon at i, compute product + run DFS on ALL other indcies that have not been used
        # return max result we get from DFS call 

        # run this DFS starting at eahc index from 0 to n-1 to find the best val we can get from starting the pop from any of these ballons and building optimal path from these


        visited = set()
        n = len(nums)
        def dfs(i, visited):

            curr = nums[i]
            left = 1 
            right = 1

            l = i-1
            r = i+1

            while l >= 0:
                if l in visited:
                    l -= 1
                else:
                    left = nums[l]
                    break

            while r < n:
                if r in visited:
                    r += 1
                else:
                    right = nums[r]
                    break
            
            product = left * curr * right

            visited.add(i)
            res = product
            for j in range(n):
                if j not in visited:
                    res = max(res, product + dfs(j, visited))
            visited.remove(i)

            return res

        res = 0
        for i in range(n):
            res = max(res, dfs(i, visited))
        return res 
        
