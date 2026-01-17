class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adj_list based on input n and edges arr
        # have a visited set to keep track of nodes visited so far
        # run DFS on adj_list of nodes, if node is marked as visited from a prev DFS call, then it's in the same component and we skip
        # otherwise we do run DFS on a node that is not visited and increment a counter
        # return counter at thr end 
    
        # time: O(v+e) due to making of v nodes and adding e edges 
        # space: O(v+e) due to adj_list storing v nodes and e edges within
        
        adj_list = {i:[] for i in range(n)}

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            neighbors = adj_list[node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        
        counter = 0
        for node in adj_list:
            if node not in visited:
                dfs(node)
                counter += 1
        return counter