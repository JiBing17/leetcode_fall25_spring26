class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        self.res = [] # final arr to return 
        nums.sort() # sort to skip pass dups
        def dfs(i,sub): # helper dfs func to populae res arr
            if i > len(nums) - 1: # exhausted list, add curr sub arr to res
                self.res.append(sub.copy())
                return 
            sub.append(nums[i]) # case where we choose to add curr num to sub arr
            dfs(i+1, sub)

            sub.pop() # case where we choose NOT to use that num so we skip to next num that is NOT the same val as curr num
            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            dfs(j, sub) 

        dfs(0,[]) # init call to helper
        return self.res # return populated res at end