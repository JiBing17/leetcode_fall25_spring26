class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = [] # final res arr to return
        self.used = [False for i in range(len(nums))] # arr used to determine which nums we have used already

        def dfs(sub): # helper dfs to populate res arr
            if len(sub) == len(nums): # reached targeted size, add that perm into res arr
                self.res.append(sub.copy())
                return

            for i, num in enumerate(nums): # for each num in nums
                if self.used[i] == True: # if we have it in sub, then skip to next num
                    continue
                sub.append(nums[i]) # otherwise we decide to use curr num in sub
                self.used[i] = True # set used to true for that num
                dfs(sub) # recursively call on new sub 

                sub.pop() # restore used and sub for next iteration when we decide to use another num in sub instead
                self.used[i] = False
 
        dfs([]) # run helper to populate res arr
        return self.res # return the populated res arr