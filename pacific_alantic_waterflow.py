class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r,c = len(heights), len(heights[0]) # define num of cols and rows for 2d matrix
        alantic = set() # i,j pairs that touch alantic 
        pacific = set() # i,j pairs that touch pacific
        res = [] # res arr to return 

        def dfs(i,j, visited, prev_val): # dfs to traverse 
            # curr pos not in bound or already seen
            if i < 0 or i >= r or j < 0 or j >= c or (i,j) in visited: 
                return
            # curr pos is not valid (water wont flow)
            if prev_val > heights[i][j]:
                return 

            # otherwise record curr pos in starting set
            visited.add((i,j))

            dfs(i+1, j, visited, heights[i][j]) # evaluate pos to bottom of curr
            dfs(i-1, j, visited, heights[i][j]) # evaluate pos to top of curr
            dfs(i, j+1, visited, heights[i][j]) # evaluate pos to right of curr
            dfs(i, j-1, visited, heights[i][j]) # evaluate pos to left of curr

        for i in range(r): 
            dfs(i,0, pacific, heights[i][0]) # run dfs on all pos touching pacific on left side
            dfs(i, c-1, alantic, heights[i][c-1]) # run dfs on all pos touching alantic on right side
        for i in range(c):
            dfs(0,i, pacific, heights[0][i]) # run dfs on all pos touching pacific on top 
            dfs(r-1, i, alantic, heights[r-1][i]) # run dfs on all pos touching alantic on bot
        
        for i in range(r): # evaluate each pos in matrix
            for j in range(c):
                # if pos reached both sets/oceans, then add to res arr 
                if (i,j) in pacific and (i,j) in alantic: 
                    res.append([i,j])
        return res # return res arr at end