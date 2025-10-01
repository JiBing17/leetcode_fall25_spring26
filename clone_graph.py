"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: # no node, return None 
            return None

        old_to_new = {} # map old node to new copy of node

        def dfs(node): # dfs for populating the hash map
            if node in old_to_new: # if curr node has a new cpy already 
                return old_to_new[node] # just return the new cpy of that node
            
            new_node = Node(node.val) # otherwise create new cpy
            old_to_new[node] = new_node  # add to the mapping

            for neighbor in node.neighbors: # for each neighboring node of curr node 

                # run dfs to make those node's new 
                # or its already created so just give us the new node instance 
                # and add to new node's neighnor
                new_node.neighbors.append(dfs(neighbor)) 
            return new_node # return new node just created 
            
        dfs(node) # run dfs on the head of the node       
        return old_to_new[node] # return head of the new node