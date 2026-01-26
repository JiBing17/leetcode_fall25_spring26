class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # efficient sol with O(v) space instead of O(v+e) from below solution, just keep track of node's incommign and outgoing edges and return the 1 with n-1 incomming edges (everyone trusts this person) and no outgoing edges(judge trusts no one)
        out_going = {}
        in_comming = {}

        for u,v in trust:
            if u not in out_going:
                out_going[u] = 0
            out_going[u] += 1 
            if v not in in_comming:
                in_comming[v] = 0
            in_comming[v] += 1 
        
        for i in range(1, n+1):
            if in_comming.get(i, 0) == n - 1 and out_going.get(i, 0) == 0:
                return i
        return -1

        # represent ppl as nodes and trust arr as edges
        # if a node has a edge coming out, then it CANT be the judge
        # if a node doesnt have ALL other node's outgoing edges to it, then it also CANT be the judge

        # form adj_list from input
        # if a node has no outgoing edges then it CAN be a judge.
        # then that node needs to appear as a node for ALL other node's outgoing edges, if not return -1 otherwise once algorithm is done return that node's number

        # time : O(v+e)
        # space: O(v+e)

        adj_list = {}

        for i in range(1, n+1): # O(v + e)
            adj_list[i] = []
        for u,v in trust:
            adj_list[u].append(v)
        
        potential_judge = -1

        for node in adj_list: # v 
            if not adj_list[node] and potential_judge == -1:
                potential_judge = node
            elif not adj_list[node] and potential_judge != -1:
                return -1
        
        for node in adj_list: # v 
            if node != potential_judge:
                neighbors = adj_list[node]
                found = False 

                for neighbor in neighbors: # e 
                    if neighbor == potential_judge:
                        found = True
                if not found:
                    return -1
        return potential_judge