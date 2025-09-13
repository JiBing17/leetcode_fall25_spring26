# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: # no tree, no right side nodes
            return []

        res = [] # arr of node val's on the right of tree 
        q = collections.deque() # deque for storing nodes on each level
        q.append(root) # add root to deque to start 

        while q: # while there are nodes to process
            q_len = len(q) # get number of nodes at current level
            for i in range(q_len): # process each node
                node = q.popleft() # get curr node
                if node: # if not leaf node 
                    if q_len - 1 == i: # if it's the last node in the curr level, then it's the right most node 
                        res.append(node.val) # add to res array 
                    if node.left: # if curr node has left child, add it to deque for next level computation
                        q.append(node.left) 
                    if node.right: # if curr node has right child, add it to deque for next level computation
                        q.append(node.right)
        return res # return res at end