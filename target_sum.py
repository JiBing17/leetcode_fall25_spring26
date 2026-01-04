class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # optimal solution - DFS with memo
        # save the computed res in hashmap of (i,curr_sum) to prevent recomputing 

        n = len(nums)
        dp = {}

        def dfs(i, curr_sum):

            if (i,curr_sum) in dp: # return already computed val
                return dp[(i, curr_sum)]
            
            if i == n:
                if curr_sum == target:
                    return 1
                else:
                    return 0

            dp[(i, curr_sum)] = dfs(i+1, curr_sum + nums[i]) + dfs(i+1, curr_sum - nums[i]) # store res of curr call
            return dp[(i,curr_sum)] 

        return dfs(0, 0)

        # brutefoce - DFS to make the decision tree
        # for curr num at i, recurse with it either being - or + and update curr sum
        # once currsum == target - return 1 
        # otherwise if we used up all numbers or curr sum > target return 0


        def dfs(i, curr_sum):
            if i == n:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            return dfs(i+1, curr_sum + nums[i]) + dfs(i+1, curr_sum - nums[i])
        
        return dfs(0, 0)


                
