class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp way
        # dp[i][j] would mean the num of unique paths to reach pos i,j
        # set 2d dp to ALL 0s
        # set dp[0][0] = 1 (starting point, 1 way to get there)
        # for every other pos i,j we could have gotten there from up OR left of curr pos
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] - if in bounds
        # return dp[m-1][n-1]

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]



        # brute-force way
        # try every possible path using DFS with i,j pos
        # for every pos, return if out of bounds return 0 
        # if at m-1, n-1 - then return 1 (or increment global counter by 1)
        
        
        def dfs(i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1


            return dfs(i+1,j) + dfs(i, j+1)

              
        return dfs(0,0)



