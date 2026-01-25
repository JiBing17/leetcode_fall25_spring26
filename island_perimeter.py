class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # have exactly 1 island in grid
        # find the perimter of that 1 island
        # run a DFS starting at the first land cell and keep track of positon (i,j) that we have visited already 
        # for each pos, if pos is out of bounds or is water then we want to just return 1 (went to an edge of the island)
        # if land cell, just mark as visited and run DFS on left, right, top, and down and make sure to return the sum that we get from those
        

        # time: O(n*m)
        # space : O(n*m) - can be O(1) if we look at all 4 directions in each cell and +1 for every water or out of bounds. 


        visited = set()
        n_rows = len(grid)
        n_cols = len(grid[0])


        def dfs(i, j, visited):
            

            if  i >= n_rows or i < 0 or j >= n_cols or j < 0 or grid[i][j] == 0:
                return 1 
            
            if (i,j) in visited:
                return 0

            visited.add((i,j))
            return dfs(i+1, j, visited) + dfs(i-1, j, visited) + dfs(i, j+1, visited) + dfs(i, j-1, visited)
        
        
        for i in range(n_rows): 
            for j in range(n_cols):
                if grid[i][j] == 1:
                    return dfs(i,j, visited)

