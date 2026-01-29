class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # optimal sol using dijkstra's 
        # have min heap to keep always give us the edge to a cell that contains the max weight of a path that is the min between all avaialbe paths
        # have a visited set to prevent going in loop
        # this way, the weight that reaches the bottom right will ALWAYS be the path that contains the min effort (max diff between any adjacent cells in that path) of all paths

        # time: O(m*n* log(m*n))
        # space: O(m*n)


        n_rows = len(heights)
        n_cols = len(heights[0])
        visited = set()
        min_q = []
        heapq.heapify(min_q)
        min_q.append((0,0,0))

        while min_q:

            diff, i, j = heapq.heappop(min_q)

            if (i,j) in visited: # prevent evaluating a cell if a better path already evaluated it already
                continue
            
            if i == n_rows - 1 and j == n_cols - 1: # return the max diff between any adjacent cells for the path that reached here first (minheap to find min of all max diffs)
                return diff
            
            visited.add((i,j)) # mark curr cell as evaluated

            if i+1 < n_rows and (i+1, j) not in visited: # if we can go down and we havent found a path that evaluated it yet
                new_diff = max(diff, abs(heights[i][j] - heights[i+1][j])) # update the max diff if needed
                heapq.heappush(min_q, (new_diff, i+1, j)) # add to min q 

            if i-1 >= 0 and (i-1, j) not in visited: # if we can go up and we havent found a path that evaluated it yet
                new_diff = max(diff, abs(heights[i][j] - heights[i-1][j]))
                heapq.heappush(min_q, (new_diff, i-1, j))

            if j+1 < n_cols and (i, j+1) not in visited: # if we can go right and we havent found a path that evaluated it yet
                new_diff = max(diff, abs(heights[i][j] - heights[i][j+1]))
                heapq.heappush(min_q, (new_diff, i, j+1))

            if j-1 >= 0 and (i, j-1) not in visited: # if we can go left and we havent found a path that evaluated it yet
                new_diff = max(diff, abs(heights[i][j] - heights[i][j-1]))
                heapq.heappush(min_q, (new_diff, i, j-1))
            


        # given n*m grid and want to find a path from top left corner to bottom right corner
        # we want to find the path that contains the min diff of the max abs diff between any cell in path

        # brute force way using DFS
        # starting from cell i,j - we move ALL 4 directions and keep track of visited set to prevent going to same cell twice within 1 path
        # also keep track of max diff by saving prev cell's value 
        # once i,j reachesthe bottom right corner, return the max diff of that path
        # to complete dfs, return min between the 4 recursive calls

        n_rows = len(heights)
        n_cols = len(heights[0])
        visited = set()

        def dfs(i,j, prev, maxdiff, visited):

            if i >= n_rows or i < 0 or j < 0 or j >= n_cols or (i,j) in visited:
                return float('inf')

            maxdiff = max(maxdiff, abs(prev - heights[i][j]))

            if i == n_rows - 1 and j == n_cols - 1:
                return maxdiff
        
            visited.add((i,j))
            down = dfs(i+1, j, heights[i][j], maxdiff, visited)
            up = dfs(i-1, j, heights[i][j], maxdiff, visited)
            right = dfs(i, j+1, heights[i][j], maxdiff, visited)
            left = dfs(i, j-1, heights[i][j], maxdiff, visited)
            visited.remove((i,j))

            return min(up, down, left, right)

        return dfs(0,0,heights[0][0], 0, visited)

            
            