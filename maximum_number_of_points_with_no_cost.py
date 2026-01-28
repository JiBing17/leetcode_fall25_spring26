class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # time : O(m*n)
        # space : O(n)
 
        n_rows = len(points) # num of rows
        n_cols = len(points[0]) # num of cols

        row = points[0] # prev row 

        for r in range(1, n_rows): # for rows 1 and down
            next_row = points[r].copy() # get copy of next row 

            pre_left = [0 for i in range(n_cols)] # best score coming from LEFT side (k <= c)
            pre_right = [0 for i in range(n_cols)] # best score coming from RIGHT side (k <= c)

            pre_left[0] = row[0] # only 1 option for best score coming from left if first element

            for c in range(1, n_cols):
                pre_left[c] = max(row[c], pre_left[c-1] - 1) # otherwise we take the score from straight above (no deduction) OR the max score (with deduction) that you could've taken from the left
            
            pre_right[n_cols-1] = row[n_cols-1] # only 1 option for the best score coming from the right 

            for c in range(n_cols-2, -1,-1):
                pre_right[c] = max(row[c], pre_right[c+1] - 1) # otherwise we take the score from straight above (no deduction) OR the max score (with deduction) that you could've taken from the right
            
            for c in range(n_cols):
                next_row[c] += max(pre_left[c], pre_right[c]) # add the max between the scpres you could've gotten coming considering BOTH sides

            row = next_row # next iteration so update row
        return max(row) # find the max score from the last row
        
        # we want to maximize our points starting from 0
        # for each row we can pick a number to add
        # for every subsequent row after, do same but subtract the col diff from prev row of the new selected score

        # dfs to make every possbile path and just return the path that ends with the max profit
        # given row i, compute the curr score for this path which is currscore + points[i][j] 0 <= j <= n-1 - abs(prev_col - j) 
        # run dfs on all cols in curr row i + their computed score and take max to return

        # time: O(m*n^2) j loop on n within dfs function - dfs runs at most m*n times
        # space: O(m*n)
    

        n_rows = len(points)
        n_cols = len(points[0])
        memo = {}

        def dfs(i, prev_col):

            if i == n_rows:
                return 0
            
            if (i, prev_col) in memo: 
                return memo[(i, prev_col)]

            res = -1
            
            for j in range(n_cols):
                cost = abs(j - prev_col)
                if i == 0:
                    cost = 0
                res = max(res, points[i][j] - cost + dfs(i+1, j))
            
            memo[(i, prev_col)] = res
            return res
        
        return dfs(0, 0)