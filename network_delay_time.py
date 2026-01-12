class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = -1 # min time needed to reach all nodes given the delay weight 
        adj_list = collections.defaultdict(list) # adjacency list to represent graph
        for edge in times: # populate list (node edge[0] to node edge[1] using edge[2] weight)
            adj_list[edge[0]].append((edge[1], edge[2]))
         
        min_q = [(0, k)] # add starting distance and node to min heap
        heapq.heapify(min_q) # make min heap based on distance (1st val)
        visited = set() # set to keep track of ALL nodes visited so far 

        while min_q: # while heap is not empty 
            dis, node = heapq.heappop(min_q) # get dis and node we can reach currently
            if node in visited: # skip eval if node was already visited 
                continue

            visited.add(node) # otherwise add to visit 
            res = max(res, dis) # update overall max time after reaching curr node with curr cumulative dis

            neighbors = adj_list[node] # find ALL neighbors and distance to each one of curr node

            for neighbor in neighbors:
                if neighbor[0] not in visited: # only a to heap for eval if not seen
                    heapq.heappush(min_q, (neighbor[1] + dis, neighbor[0])) # update dis needed to reach that node (cumulative distance)
        
        if len(visited) != n: # if we did not visit ALL n nodes in graph, then return -1 for impossible to reach case
            return -1 
        return res # otherwise return min time needed to reach ALL n nodes

