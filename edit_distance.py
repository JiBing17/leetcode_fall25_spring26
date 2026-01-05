class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp way - 2d dp arr
        # dp[0][0] = min operations to make word1 into word2 starting with substring 0 to end for BOTH word1 and word2
        # dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][i+1]) if curr chars not same
        # dp[i][j] = dp[i+1][j+1] if curr chars are the same   
        # i+1 indicates we are deleting curr char at i so move i to next indice
        # j+1 means we are adding same char word2[j] has to left of curr index i so i stays the same and j moves on to eval next char
        # i+1 and j+1 means we replace curr char at index i to the same char as curr char at index j so they are same move on
        # +1 to indicate an operation was done
        # make extra row and col for "" to fill in base case if i or j becomes empty string
        # time : O(m*n)
        # space : O(m*n)
        n = len(word1)
        m = len(word2)

        dp = [[float('inf') for i in range(m+1)] for j in range(n+1)]

        for i in range(n+1):
            dp[i][m] = n - i
        for j in range(m+1):
            dp[n][j] = m - j
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    
        return dp[0][0]


        # brute force
        # keep track of curr indices for word1 (i) and word2 (j)
        # keep trakc of size of strings n and m for word1 and word2 respectively
        # DFS to decide if we want to add or remove or replace curr char at index i
        # once we know one of the indices reach the end, we know exactly how many other operations we need to make them the same (repeated add or delete)
        # O(3^ n+m)

        def dfs(i,j):
            
            if i == j == m == n:
                return 0

            if i == n:
                return m - j
            if j == m:
                return n - i
            
            if word1[i] == word2[j]:
                match = dfs(i+1 , j+1)
                return match
            else:
                insert = 1 + dfs(i,j+1)
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1,j+1)
            
                return min(insert, delete, replace)
        return dfs(0,0)




     