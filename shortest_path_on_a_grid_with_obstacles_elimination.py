class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        # bfs sol:
        # have a deque and add first position at top left corner to q
        # also add the curr k integer to keep track of how many removals we have left
        # keep a 2d array to represents the max num of removals we had once a path reached position at i,j - the key here is to only visit a positon i,j if we know we have a greater removal count than before since that will be the only way we "do better"
        # have a level counte to count BFS levels 
        # on each level add the valid neighbors to q ONLY if the number of removals we had last time we went there is < what we currently have 
        # decrement counter before adding if neighbor positon is a 1
        # this way we only revisit cells if we know the curr path has more removal opportunities than the last path that visited there had.

        # time : O(m*n*k) eval entire grid, CAN go to same cell depending on k so m*n*k
        # space : O(m*n)

        q = deque() 
        n_rows = len(grid)
        n_cols = len(grid[0])

        best = [[-1 for i in range(n_cols)] for i in range(n_rows)]

        q.append((0,0, k))
        level = 0

        while q:
            q_size = len(q)

            for i in range(q_size):
                i,j, counter = q.popleft()

                if i == n_rows - 1 and j == n_cols - 1:
                    return level
                
                if i+1 < n_rows :
                    c_down = counter - grid[i+1][j]
                    if best[i+1][j] < c_down:
                        best[i+1][j] = c_down
                        q.append((i+1, j, c_down)) 
                if i-1 >= 0 :
                    c_up = counter - grid[i-1][j]
                    if best[i-1][j] < c_up:
                        best[i-1][j] = c_up
                        q.append((i-1, j, c_up) )
                if j+1 < n_cols :
                    c_right = counter - grid[i][j+1]
                    if best[i][j+1] < c_right:
                        best[i][j+1] = c_right
                        q.append((i, j+1, c_right)) 
                if j-1 >= 0 :
                    c_left = counter - grid[i][j-1]
                    if best[i][j-1] < c_left:
                        best[i][j-1] = c_left
                        q.append((i, j-1, c_left)) 
            level += 1
        return -1
            






        # given k free removals of 1, find min steps needed to go from top left to bottom right of 2d grid
        # run DFS and try ALL possbile paths
        # keep track of num of removals we still have
        # if curr cell is a obstacle subtract from k, if k < 0, return inf 
        # also if out of bounds, return inf
        # also keep track of visited set to prevent going to same spot
        # return min of the 4 directions

        # if dfs(0,0,visited, k) == inf, return -1 otherwise return ret val

        #  time : O(4^n*m)
        #  space : O(n*m)


        n_rows = len(grid)
        n_cols = len(grid[0])

        visited = set()
        
        def dfs(i,j, visited, k):
            if i >= n_rows or i < 0 or j < 0 or j >= n_cols or (i,j) in visited:
                return float('inf')
            if i == n_rows - 1 and j == n_cols - 1:
                return 0
            if grid[i][j] == 1:
                k -= 1
                if k < 0:
                    return float('inf')

            visited.add((i,j))

            down = dfs(i+1, j, visited, k)
            up = dfs(i-1, j, visited, k)
            right = dfs(i, j+1, visited, k)
            left = dfs(i, j-1, visited, k)

            visited.remove((i,j))

            return 1 + min(up, down, left, right)
        
        res = dfs(0,0, visited, k)
        if res == float('inf'):
            return -1
        return res        