class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r,c = len(grid), len(grid[0]) # define rows and cols for 2d matrix

        self.seen = set() # set to determine which pos we have visited already
        self.sub = set() # set to determine which pos we visited for curr island traversal  
        max_area = 0 # max area to return - default 0 for no island

        def dfs(i,j): # helper dfs for traversign through 2d grid
            if (i,j) in self.seen: # don't visit already seen pos
                return
            if i < 0 or i >= r or j < 0 or j >= c: # out of bounds
                return
            if grid[i][j] == 0: # water, also dont visit
                return

            # otherwise it's land 
            self.seen.add((i,j)) # add to overall visited pos
            self.sub.add((i,j)) # add to visted for curr island (len is area of this island)
            dfs(i+1, j) # traverse down
            dfs(i-1, j) # traverse up
            dfs(i, j+1) # traverse right
            dfs(i,j-1) # traverse left
        
        for i in range(r): # for each entry row
            for j in range(c): # for each entry col

                if grid[i][j] == 1 and (i,j) not in self.seen: # if land and is apart of new island
                    self.sub.clear() # clear visted positions (area) for prev island
                    dfs(i,j) # run dfs on new island to get new area
                    if len(self.sub) > max_area: # update if curr island is bigger in area
                        max_area = len(self.sub)
        return max_area # return the biggest island found