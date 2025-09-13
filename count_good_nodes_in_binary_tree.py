# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0 # global var to store count of good nodes
        def dfs(root, max_seen): # helper dfs for traversing through tree and counting
            if not root: # leaf node, just return  
                return 
            if root.val >= max_seen: # curr node is a good node since it's >= biggest val we seen traversing down
                self.count += 1 
            max_seen = max(max_seen, root.val) # update biggest seen if needed  

            dfs(root.right, max_seen) # recursively call func on right subtree
            dfs(root.left, max_seen)  # recursively call func on left subtree 
        dfs(root, root.val) # run dfs starting from root with max seen being the root val
        
        return self.count # return the updated global count var at end