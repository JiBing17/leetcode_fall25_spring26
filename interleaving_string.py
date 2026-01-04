class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # dp way
        # dp[0][0] if possible to interleave from 0 to end of BOTH s1 and s2 to make up s3
        # if s1 and s2 are empty strings, then we CAN interleave empty strs to make up s3
        # init all vals in 2d dp to False but make extra row and col for the bottom right corner to be True for empty str case
        # do bottom up approach to fill out table with dp relation as:
            # dp[i][j] = dp[i][j] or dp[i+1][j] if s1[i] == s3[i+j] 
            # dp[i][j] = dp[i][j] or dp[i][j+1] if s2[j] == s3[i+j]

        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
            
        dp = [[False for i in range(m+1)] for j in range(n+1)]

        dp[n][m] = True

        # fill last column (s2 exhausted - True if for each s1 char, s3 char is SAME)
        for i in range(n - 1, -1, -1):
            dp[i][m] = dp[i + 1][m] and s1[i] == s3[i + m]

        # fill last row (s1 exhausted - True if for each s2 char, s3 char is SAME)
        for j in range(m - 1, -1, -1):
            dp[n][j] = dp[n][j + 1] and s2[j] == s3[n + j]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                sub1 = ""
                sub2 = ""

                if i+1 <= n:
                    sub1= dp[i+1][j]
                if j+1 <= m:
                    sub2 = dp[i][j+1]

                if s1[i] == s3[i+j]:
                    dp[i][j] = dp[i][j] or sub1
                
                if s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j] or sub2
                    
        return dp[0][0]


        # brute force using DFS to try all possbile substrings of s1 and s2 to see if they can make up s3
        # DFS will take curr char at index i and j index for s1 and s2
        # if they both reach the end then we CAN make up s3 using subs for those 2
        # try ALL paths meaning if curr char in s3 == s1's curr char then run a DFS choosing that as the sub 
        # same goes with s3 and s2's chars as well
        # otherwise if no matching chars for curr s1 and s2 for s3 OR the paths down the recursion doesn't work then return False
        # we can also use memo as well to store answer to avoid recomputation

        def dfs(i, j):
            if i == n and j == m:
                return True
            
            if i < n and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < m and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            
            return False
        
        return dfs(0,0)


                