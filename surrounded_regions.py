class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set() # positions that touch connect to an O in the outer edge of matrix
        
        r,c = len(board), len(board[0]) # num of rows and cols in matrix

        def dfs(i,j, visited): # helper dfs for adding to visited set
            if i < 0 or i >= r or j < 0 or j >= c: # position is out of bounds - just return 
                return
            if board[i][j] == "X" or (i,j) in visited: # position is X or seen alreaddy-return
                return 
            
            visited.add((i,j)) # otherwise its an O and we add it to visited 
            dfs(i+1, j, visited) # visit bottom of curr pos 
            dfs(i-1, j, visited)  # visit top of curr pos 
            dfs(i, j+1, visited) # visit right of curr pos
            dfs(i, j-1, visited) # visit  left of curr pos
        

        for i in range(r): 
            dfs(i,0, visited) # run dfs starting from left edge
            dfs(i, c-1, visited) # run dfs starting from right edge

        for i in range(c): 
            dfs(0, i, visited) # run dfs starting from top edge 
            dfs(r-1, i, visited) # run dfs starting from bottom edge
        
        for i in range(r):
            for j in range(c):
                # change all O's to X if it didn't connect to an O on the edges
                if board[i][j] == "O" and (i,j) not in visited: 
                    board[i][j] = "X"