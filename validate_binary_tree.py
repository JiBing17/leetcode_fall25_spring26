# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high): # helper dfs to tell you curr node's val is within bound of the bst restriction
            if not root: # made to end with no false, so return True (valid)
                return True

            if root.val <= low or root.val >= high: # case if curr node's val breaks bst restriction
                return False

            # recursively call on left and right subtree and adjust low / high bounds according to their ancestor node 
            # - will only return true if both subtree's are within bounds of curr node making entire curr tree valid
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high) 
        
        return dfs(root, float('-inf'), float('inf')) # run dfs on root node to inspect entire tree