class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # brute force using DFS
        # given curr index of s and t (i an j respectively)
        # if j == m return 1 (curr sequence contains all chars in t)
        # if i == n and j < m return 0 (not enough chars in s to eval in order to finish t)
        # for char at index i we can run DFS to decide if we want to include it or NOT but ONLY if char at i == char at j. If not equal, we only have option to don't include curr char at i for string s
        
        # with memo - optimal 
            # time: O(n*m)
            # space : O(n*m)
        # without memo:
            # time: O(2^n)
            # space: O(n)
        n = len(s) 
        m = len(t)
        memo = {}

        def dfs(i,j):
            if j == m:
                return 1
            if i == n and j < m:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            include = 0
            dont_include = 0

            if s[i] == t[j]:
                include = dfs(i+1, j+1)
                dont_include = dfs(i+1, j)
            else:
                dont_include = dfs(i+1, j)
            memo[(i,j)] = include + dont_include
            return memo[(i,j)]

        return dfs(0,0) 
             