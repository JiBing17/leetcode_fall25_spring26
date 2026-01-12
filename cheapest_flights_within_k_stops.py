class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman-ford to find shortest path to the nodes based on evaluation on edges
        # constraint is we can have at most k stops in between src and dst so we only update the path after each iteration from i to k. That way we only look at the paths available to us iteration by iteration 
            # have dis arr to indicate shortest dis needed to reach nodes 
            # init node src to 0
            # for each iteration, look at ALL edges and see if there is a new shortest dis to reach there, 
            # if yes, update temp dis arr AND ONLY update actual dis arr at end of each iteration
            # at end return dis[dist] or -1 if slot is still infinity (not reachable)

            # time : O(e*k) where e = total number of edges
            # space: O(n) where n = total number of nodes/cities given

        dis = [float('inf') for i in range(n)] # distance arr to see shortest path to get to a certain node 0 to n-1
        dis[src] = 0 # src node is start so distance to get there is 0

        for i in range(k+1): # for k stops in between src and dst 
            tmp = dis.copy() # have tmp cpy of dis arr to update after each iteration 
            for arr in flights: # for each edge from node i to node j 

                curr = arr[0] # get the node the edge is comming from
                des = arr[1] # get node the edge is pointing to 
                distance = arr[2] # get weight of that edge 
            
                if distance + dis[curr] < tmp[des]: # if distnace to get to that node curr at that current leve + edge to get to node des is SHORTER than any other path seen so far at curr level, than update the tmp arr for the node des (new fastest way to reach there for curr level / stop i)
                    tmp[des] = distance + dis[curr]
            dis = tmp # only update the distance arr for each level at end 
        if dis[dst] == float('inf'): # not possbile to reach dst node at end of loop
            return -1
        return dis[dst] # otherwise return the shortest needed using updated dis arr

