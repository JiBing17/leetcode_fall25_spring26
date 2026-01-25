class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # run DFS to make all possibles subsets and within these subsets, xor them and add result to a global sum

        # time: O(2^n * n)
        # space: O(n)

        self.total = 0
        n = len(nums)

        def dfs(i, path): 
            if i == n:
                res = 0
                for num in path:
                    res = res ^ num  
                self.total += res
                return
            
            curr_num = nums[i] 
            path.append(curr_num)
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path) 
        
        dfs(0, [])
        return self.total