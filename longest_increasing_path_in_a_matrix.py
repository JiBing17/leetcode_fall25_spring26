class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        # brute force using DFS
        # given pos (i,j) we can return 0 if out of bounds or prev num > curr num or pos alreadu in visited
        # otherwise we return 1 + min of going up, down, left, or right
        # for each cell in matrix, run DFS and save max length overall 
        # time: O(n*m*3^(n*m))
        # space : O(1)
        
        # optimal way: use memoization to prevent recompuaton of same calls
        # time : O(n*m)
        # space: O(n*m)

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        memo = {}

        def dfs(i, j, prev):

            if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
                return 0

            curr = matrix[i][j]
            if prev >= curr:
                return 0

            if (i, j) in memo:
                return memo[(i,j)]

            
            down_op = dfs(i+1,j, curr)
            up_op = dfs(i-1,j, curr)
            right_op = dfs(i,j+1, curr)
            left_op = dfs(i,j-1, curr)


            memo[(i,j)] = 1 + max(down_op, up_op, right_op, left_op)
            return memo[(i,j)]

        res = 1
        for r in range(n_rows):
            for c in range(n_cols):
                res = max(res, dfs(r, c, matrix[r][c]-1))
        return res
    

