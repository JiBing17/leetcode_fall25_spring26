class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        # BFS approach - start from chest positions
        # time : O(n*m)
        # space: O(n*m)

        # run BFS and store ALL chest pos in deque (priority queue)
        # from there have visited set to prevent visiting same pos multiple times
        # pop positions layer by layer and updated land cell to that layer count (shortest time for that cell to get to chest)
        # add all land cells that we have not seen yet of that curr pos we just popped to compute next layer
         

        q = deque()
        n_rows = len(grid)
        n_cols = len(grid[0])

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        visited = set() 
        counter = -1
        while q:
            counter += 1
            q_size = len(q)
            for k in range(q_size):
                
                
                i,j = q.popleft()

                if (i,j) in visited:
                    continue
                visited.add((i,j))
                grid[i][j] = counter
                
                if i+1 < n_rows and grid[i+1][j] != -1 and grid[i+1][j] != 0 and (i+1,j) not in visited:
                    
                    q.append((i+1,j))
                if i-1 >= 0 and grid[i-1][j] != -1 and grid[i-1][j] != 0 and (i-1,j) not in visited:
                    q.append((i-1,j))
                if j+1 < n_cols and grid[i][j+1] != -1 and grid[i][j+1] != 0 and (i,j+1) not in visited:
                    q.append((i,j+1))
                if j-1 >= 0 and grid[i][j-1] != -1 and grid[i][j-1] != 0 and (i,j-1) not in visited:
                    q.append((i,j-1))   
        return
                            

                


        # brute force - explore every possbile path from every land cell and keep min dis to reach treasure along each call
        # time : O((n*m) * 3^(n*m)) - 3 and not 4 because cant revisit same pos
        # space: O(n*m) - visited set can contain ALL pos in grid (snake like path) worst case 
        # use dfs on each land cell and find ALL possbile paths  while keeping count of num of moves until we either return inf (impossible case)
        # or we return a num which represents how many steps were needed to get to a treasure chest in that path
        # take min of those paths and store answer in hash map (i,j) for us to populate the input arr at end
        visited = set()
        n_rows = len(grid)
        n_cols = len(grid[0])


        def dfs(i,j, visited, dis):
            if i >= n_rows or i < 0 or j >= n_cols or j < 0 or (i,j) in visited:
                return float('inf')

            if grid[i][j] == -1:
                return float('inf')
            if grid[i][j] == 0:
                return dis

            visited.add((i,j))
            up_dis = dfs(i-1, j, visited, dis + 1)
            down_dis = dfs(i+1 , j, visited, dis + 1)
            right_dis = dfs(i, j+1, visited, dis+1)
            left_dis = dfs(i, j-1, visited, dis+1)

            visited.remove((i,j))
            
            return min(up_dis,down_dis, right_dis, left_dis)
        
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == -1 or grid[i][j] == 0:
                    continue
                else:
                    grid[i][j] = dfs(i,j, visited, 0)