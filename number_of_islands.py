class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r,c = len(grid), len(grid[0]) # get row and col vals for 2d grid
        self.seen = set() # seen set to keep track of what i,j pairs we have visted
        self.count = 0 # count of unqiue islands

 
        def dfs(i,j, seen): # dfs func to traverse through grid
            if (i,j) in seen: # don't visit already seen pos 
                return  
            if i < 0 or i >= r or j < 0 or j >= c: # out of bounds / not valid pos
                return 

            if grid[i][j] == "0": # water nothing to visit
                return
            
            seen.add((i,j)) # otherwise it's land so add to visit set
            
            dfs(i+1,j, seen) # traverse down
            dfs(i, j+1, seen) # traverse right
            dfs(i-1, j, seen) # traverse up 
            dfs(i, j-1, seen) # traverse left

        for i in range(r): # for each row in grid 
            for j in range(c): # for each col in grid 
                if (i,j) not in self.seen and grid[i][j] == "1": # if land and we haven't marked it has visted from prev dfs traversal. traverse entire land expansion and add to seen
                    dfs(i,j, self.seen)
                    self.count += 1 # incrememet island count
        return self.count # ret island count at end