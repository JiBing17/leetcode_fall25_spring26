class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = [] # final arr to return 
        self.curr_path = [] # arr to append curr selected subset 

        def dfs(i): # helper dfs with i as index of val in nums to add or not
            if i >= len(nums): # base case : went through entire nums arr  - add the subset comb we made 
                self.res.append(self.curr_path.copy()) # copy() to prevent mutation on other calls
                return 
            self.curr_path.append(nums[i]) # case if we decide to include val at index i in nums in subset
            dfs(i+1) # recursively call and evaluate on next val

            self.curr_path.pop() # case if we DONT decide to include val at index i in nums in subset
            dfs(i+1) # recursively call and evaluate on next val

        dfs(0) # run helper starting from index 0 of nums arr 

        return self.res # return the populate res 