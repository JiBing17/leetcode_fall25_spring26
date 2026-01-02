class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # 2d dp arr to represent LCS given substr i to end and j to end
        # init all values to 0
        # in order to compute dp[i][j], if curr chars match then its +1 and what ever the follwing chars are dp[i+1][j+1]
        # if NOT same, then max can only be if we look at the next char at i+1 or next char at j+1 
        # return dp[0][0]

        dp = [[0 for i in range(len(text2))] for j in range(len(text1))] # init 2d dp arr
        
        for i in range(len(text1)-1,-1,-1): # from bottom up
            for j in range(len(text2)-1, -1, -1): # from right to left

                # init LCS for these 3 calls (val for out of bounds case)
                right = 0
                down = 0
                diag = 0 

                if j + 1 < len(text2): # if we could get LCS from right cell
                    right = dp[i][j+1] # get LCS there
                if i + 1 < len(text1): # if we can get LCS from bottom cell
                    down = dp[i+1][j]
                if i+1 < len(text1) and j+1 < len(text2): # if we can get LCS from diag
                    diag = dp[i+1][j+1]
                
                if text1[i] == text2[j]: # if curr chars match +1 and see what the subproblem ahead of those 2 chars say
                    dp[i][j] = 1 + diag
                else: # otherwise, we would look at the path where we include/ not include one of the two chars
                    dp[i][j] = max(down, right)

        return dp[0][0] # return LCS starting from i (and j) to end for BOTH str i and j



        # brute force
        # DFS to comapre every possible subsequence
        # if curr char i and j of text1 and text2 are same , +1 and try the next 2 chars 
        # otherwise try the other possbile options char at i+1 and j OR char at i and j+1
        # return the max count of those in that case 

        
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0,0)
        
        