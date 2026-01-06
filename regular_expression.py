class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      
        # brute force solution using DFS given index i and j for strings s and p
        # before checking if curr chars are the same, we want to check if char after the curr char at index j of p has a "*"
        # if so we run DFS to either skip char + "*" or if chars match rn, try adding 1 of that char to path
        # otherwise if no "*" after curr char at index j AND curr chars still match, then run DFS evaluating the next 2 chars for the 2 strings
        # otherwise return False since we can't match since curr 2 chars are NOT he same
        # time  : O(2^(n + m))   (exponential due to branching on '*')
        # space : O(n + m)       (recursion stack)

        # dp way using memo
        # have map to map (i,j) to their answer (T/F) to avoid recomputation of same call
        # time : O(m*n)
        # space : O(m*n)

        n = len(s)
        m = len(p)
        memo = {}

        def dfs(i,j):
            if i >= n and j >= m:
                return True
            if j >= m:
                return False
            
            if (i, j) in memo:
                return memo[(i,j)]

            match = False

            match = (i < n and (s[i] == p[j] or p[j] == "."))

            if j+1 < m and p[j+1] == "*":
                res = ( dfs(i, j+2) or (match and dfs(i+1, j)) )
                memo[(i,j)] = res
                return res
            if match:
                res =  dfs(i+1, j+1)
                memo[(i,j)] = res
                return res
            memo[(i,j)] = False
            return False

        return dfs(0,0)    
            