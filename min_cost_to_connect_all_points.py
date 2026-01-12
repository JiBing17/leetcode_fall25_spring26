class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # time: O(n^2 * logn) # adding edges to heap and poping (prim's)
        # space: O(n^2) - adjlist can have at most n^2 edges where n = total num of nodes


        n = len(points) # num of points
        adj_list = {i:[] for i in range(n)} # make adjlist to represent graph 
        
        for i in range(n-1): # populate adjlist using the dis formula for edge weight
            x,y = points[i]
            for j in range(i+1, n):
                x_2, y_2 = points[j]
                dis = abs(x_2 - x) + abs(y_2 - y)
                adj_list[i].append((dis, j)) 
                adj_list[j].append((dis, i))
        
        # prims
        res = 0 # init total edge weight for MST
        visited = set() # prevent eval same node
        min_q = [(0, 0)] # add first node and dis to get there at start
        heapq.heapify(min_q) # make min heap

        while len(visited) < n: # while we haven't visited ALL nodes yet
            dis, node = heapq.heappop(min_q) # pop curr node and dis to get there to eval
            if node in visited: # if eval already, skip
                continue
            
            visited.add(node) # otherwise add to visit
            res += dis # that distance is min edge weight to get there so add to res
            neighbors = adj_list[node] # find all neighbors of curr node

            for neighbor in neighbors:
                if neighbor[1] not in visited: # add to heap if not eval already 
                    heapq.heappush(min_q, (neighbor[0], neighbor[1])) # add distance to reach those nodes from curr node as well as that neighbor's node num
        return res # return res at end of algorithm