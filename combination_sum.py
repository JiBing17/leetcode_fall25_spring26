class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = [] # final arr to return 
        self.sub = [] # subset arr for curr choices 

        def dfs(i, target): # helper dfs for appending combs to res arr 
            if target == 0: # based case - reached target, append the subarray that acheived this
                self.res.append(self.sub.copy())
                return 
            if i >= len(candidates) or target < 0: # overshot target or exhausted candidates list - just return 
                return 

            self.sub.append(candidates[i]) # case 1: we decide to use curr val 
            dfs(i, target - candidates[i]) # recursively call it with updated target and the choice to use curr val again

            self.sub.pop() # case 2: we decide to NOT use curr val 
            dfs(i+1, target)  # recursively call it with same target val and move on the next candidate val

        dfs(0, target) # start helper with first val in candidate and the init target 
        return self.res # return the populated res after recursive call