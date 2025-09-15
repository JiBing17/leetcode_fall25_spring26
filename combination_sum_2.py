class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = [] # final arr array
        self.sub = [] # sub arr for that combination path 
        candidates.sort() # sort to process and skip dups in loop time

        def dfs(i, target): # helper func to populate sub arr

            if target == 0: # sub arr satisfies condition 
                self.res.append(self.sub.copy()) # add sub arr to final arr
                return
            if i > len(candidates) - 1 or target < 0: # exhausted candidates list or overshot the target in curr path, N/A
                return

                
            self.sub.append(candidates[i]) # select curr num as a potential comb
            dfs(i+1, target - candidates[i]) # evaluate again with the remaining nums 
            j = i + 1 # next num index for not selecting curr num
            # update that index if next num is same as the one we are skipping currently
            while j < len(candidates) and candidates[j] == candidates[i]: 
                j += 1 
            self.sub.pop() 
            dfs(j, target) # run helper in the case we decide not to use curr num at all 

          
        dfs(0, target) # call hlper func to populate res arr 
        return self.res # return the populate res arr at end