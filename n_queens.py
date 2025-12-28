class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.res = [] # global arr used to store the possible boards
        board = [["."] * n for i in range(n)] # make nxn board with all "."

        col = set() # keep track of which Queens are placed in which column
        pDiagonal = set() # keep track of Queens placed within each positive diagonal
        nDiagonal = set() # keep track of Queens placed within each negative diagonal 

        def dfs(r): # DFS to find all valid boards 
            if r == n: # if we processed all rows 
                path = ["".join(row) for row in board] # add te curr board to arr
                self.res.append(path) # add arr to global arr 
                return # exit imediatly
            
            for c in range(n): # for each col within curr row 
                if c in col or (r+c) in pDiagonal or (r-c) in nDiagonal: # if not valid spot to place Q, skip it 
                    continue
                
                # otherwise...
                board[r][c] = "Q" # place Queen  
                col.add(c) # mark col as used 
                pDiagonal.add((r+c)) # mark postive diagonal as used
                nDiagonal.add(r-c) # mark negative diagonal as used

                dfs(r+1) # continue to next row after making our choice for curr row 

                # back track and so we can try another col trying this col 
                board[r][c] = "." 
                col.remove(c)
                pDiagonal.remove((r+c))
                nDiagonal.remove(r-c)

        dfs(0) # start DFS from first row in board
        return self.res # return the populated global arr at end of DFS
