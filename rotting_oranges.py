class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r,c = len(grid), len(grid[0]) # get num of cols and rows of the input grid
        q = deque() # deque for bfs
        fresh = 0 # num of fresh oranges
        time = 0 # keep track of mins 

        for i in range(r):  # for each row 
            for j in range(c): # for each col
                if grid[i][j] == 2: # if its a rotten orange 
                    q.append((i,j)) # add position to queue as one of the starting points
                if grid[i][j] == 1: # if its a fresh orange
                    fresh += 1 # add to the fresh orange counter

        if fresh == 0: # no fresh oranges in grid, return 0 in that case
            return 0

        # otherwise perform bfs 
        while q: # while queue is not empty... 
            q_len = len(q) # get length of queue for that computation of items in that layer
            spread = False # indicate if we rotten a orange during computation below
            for i in range(q_len):
                curr = q.popleft() # evaluate curr rotten orange

                # if we can rotten the orange below curr rotten one
                if curr[0] + 1 < r and grid[curr[0] + 1][curr[1]] == 1:
                    q.append((curr[0] + 1, curr[1])) # add to queue for next layer eval
                    grid[curr[0] + 1][curr[1]] = 2  # change to rotten to prevent eval again 
                    fresh -= 1 # decrement fresh count 
                    spread = True # made at least one orange rotten, change spread bool to True

                # same case but for evaluating orange above curr rotten one
                if curr[0] - 1 >= 0 and grid[curr[0] -1][curr[1]] == 1:
                    q.append((curr[0] -1, curr[1]))
                    grid[curr[0] -1][curr[1]] = 2
                    fresh -= 1
                    spread = True

                # same case but for evaluating to left of curr rotten one
                if curr[1] + 1 < c  and grid[curr[0]][curr[1] +1] == 1:
                    q.append((curr[0], curr[1] + 1))
                    grid[curr[0]][curr[1] +1] = 2 
                    fresh -= 1
                    spread = True

                # same case but for evaluating to right of curr rotten one
                if curr[1] - 1 >= 0 and grid[curr[0]][curr[1] - 1] == 1:
                    q.append((curr[0], curr[1] - 1))
                    grid[curr[0]][curr[1] - 1] = 2
                    fresh -= 1
                    spread = True
            # only if we "spread" rotteness to another orange do we increment the min
            if spread:
                time += 1
        if fresh > 0: # if there are still fresh oranges left, return -1 
            return -1
        return time # otherwise return min minutes to rotten all oranges