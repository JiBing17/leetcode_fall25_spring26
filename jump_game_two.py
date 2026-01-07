class Solution:
    def jump(self, nums: List[int]) -> int:

        # greedy way using BFS:
        # for each level, expand window for the next level using l and r pointers
        # +1 to jump for each level
        # once r pointer reaches n-1 we have offically finished
        # greedy part: we delay the jump until we evaluated all our options for that level to make the furthest jump (r+1) for evaluating next level
        # time : O(n)
        # space : O(1)
        
        n = len(nums) # num of elemens in nums

        # init l and r pointers
        l = 0
        r = 0

        max_reached = 0 # furthest possible jump so far 
        res = 0 # min num of jumps needed

        while r < n-1: # while we haven't reached the last spot
            for i in range(l, r+1): # evaluation all position we can start jump from
                max_reached = max(max_reached, i + nums[i]) # update farthest we can jump to 

            l = r+1 # set window start to prev window end + 1
            r = max_reached # set window end to farthest we can reach
            res += 1 # add 1 to jump
        return res # return min jumps at end

        # brute force way using DFS to try all possible paths  
        # time : O(m^n)
        # space: O(n)


        n = len(nums) 

        def dfs(i):
            if i == n-1:
                return 0
            if i >= n:
                return float('inf')

            n_jumps = nums[i]

            if n_jumps == 0:
                return float('inf')
            
            min_jumps = float('inf')
            
            for j in range(i+1, i+1 + n_jumps):
                min_jumps = min(min_jumps, 1 + dfs(j))
            
            return min_jumps

        return dfs(0)

       
            



