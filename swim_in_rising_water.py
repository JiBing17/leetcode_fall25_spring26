class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # time: O(n^2 * logn)
        # space: O(n^2)
        
        # use a version of djiksra's algorithm to find path with cheapest nums to get to the bottom right corner and keep track of the max num seen from that path
        # that num is the answer we want to solve this solution

        r = len(grid) # get num of rows
        c = len(grid[0]) # get num of cols
        visited = set() # set to prevent visiting same pos

        min_heap = [(grid[0][0], (0,0))] # using a version djikstra's algorithm
        heapq.heapify(min_heap)  # make heap

        while min_heap: # while heap is not empty
            dis, pos = heapq.heappop(min_heap) # find max num seen in curr path and pos 
            if pos in visited: # if we already visited pos, skip 
                continue

            visited.add(pos) # otherwise add it to visited set

            i, j = pos # get curr pos
            if i == r-1 and j == c-1: # if bottom right corner
                return dis # return the max num seen in curr path 

            if i+1 < r and (i+1, j) not in visited: # if we can traverse down
                max_seen = max(dis, grid[i+1][j]) # update max num seen in going down
                heapq.heappush(min_heap, (max_seen, (i+1, j))) # add to heap the pos and updated num

            # same for up case 
            if i-1  >= 0 and (i-1, j) not in visited:
                max_seen = max(dis, grid[i-1][j])
                heapq.heappush(min_heap, (max_seen, (i-1, j)))

            # same for right case
            if j+1 < c and (i, j+1) not in visited:
                max_seen = max(dis, grid[i][j+1])
                heapq.heappush(min_heap, (max_seen, (i, j+1)))

            # same for left case
            if j-1 >= 0 and (i, j-1) not in visited:
                max_seen = max(dis, grid[i][j-1])
                heapq.heappush(min_heap, (max_seen, (i, j-1)))

            




        # brute force solutuin
        # find ALL posible paths and keep track of max val seen within each path
        # find overall max of all paths and return that 
        # use memo to reduce same DFS calls

        # time : O(n^2 * n^2) where n is size of rows and cols in input grid (other n^2 for possbile max_time vals)
        # space: O(n^4) 
        r = len(grid)
        c = len(grid[0])
        visited = set()
        memo = {}

        def dfs(i,j, max_time):

            if i >= r or i < 0 or j >= c or j < 0:
                return float('inf')
            if (i,j) in visited:
                return float('inf')
            if i == r - 1 and j == c - 1:
                max_time = max(max_time, grid[i][j])
                return max_time
            if (i, j, max_time) in memo:
                return memo[(i, j, max_time)]
            
            max_time = max(max_time, grid[i][j])

            visited.add((i,j))
            
            down_res = dfs(i+1, j, max_time)
            up_res = dfs(i-1, j, max_time)
            right_res = dfs(i,j+1, max_time)
            left_res = dfs(i, j-1, max_time)

            visited.remove((i,j))
            res = min(down_res, up_res, right_res, left_res)
            memo[(i, j, max_time)] = res
            return res
        return dfs(0,0, -1)
            

            