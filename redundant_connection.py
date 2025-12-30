class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find to detect first occurenc of cycle using input edges
        # union two nums of the same group = cycle detection

        n = len(edges) # cycle == num of edges = num of nodes

        parent = [i for i in range(n+1)] # each node points to itself
        rank = [1 for i in range(n+1)] # each group is size 1 initially (1 node per group)
        def find(n1): # find parent of passed in node
            if n1 == parent[n1]: # if itself, just return node
                return parent[n1]
            else: # otherwise if not itself ...
                parent[n1] = find(parent[n1]) # keep finding parent of the parent 
                return parent[n1] # return parent

        def union(n1,n2): # grouping the nodes using union

            p1, p2 = find(n1), find(n2) # find parent of the two nodes

            if p1 == p2: # if same parent, then both in same group, return False (cycle detected)
                return False
            if rank[p1] > rank[p2]: # otherwise if group 1 is bigger 
                parent[p2] = p1 # combine group 2 to group 1 
                rank[p1] += rank[p2] # update size of group 1 
            else: # othercase
                parent[p1] = p1 
                rank[p2] += rank[p1]

            return True # return True indicating no cycle is detected 

        for n1, n2 in edges: # for each edge from n1 to n2 ...  
            if not union(n1,n2):  # union those 2 nodes and if any are in group together
                return [n1,n2] # then there is a cycle that will be detected