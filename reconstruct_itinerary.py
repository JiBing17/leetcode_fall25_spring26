class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # time : O(eloge) - sorting input tickets which represent edges
        # space : O(v+e) or O(e) 
        # The adjacency list stores one key per source airport and one list entry per ticket, so its space complexity is O(V + E), which simplifies to O(E) since V ≤ E + 1.


        adj = defaultdict(list) # make adjacency list to represent graph based on input 
        tickets.sort(reverse=True) # sort in descedning order of strings
        for src, dest in tickets: # build graph
            adj[src].append(dest)

        res = [] # arr to return at end

        def dfs(src): # func to explore graph 
            
            while adj[src]: # while curr node as neighbors
                next_dest = adj[src].pop() # find the bigger lexical string 
                dfs(next_dest) # explore their neighbors
            res.append(src) # once at end, add curr node to res (result in bigger lexical order first AND is added from end trip to start)

        dfs("JFK") # populate res from end trip to start trip in biger lexical order 
        
        return res[::-1]  # return the res arr in reverse order so its in smaller lexical order 

