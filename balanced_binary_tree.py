# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True # globar var to indicate if tree is stil balanced

        def dfs(root): # helper dfs function to traverse through the tree
            if not root: # leaf node, return 0 for height
                return 0
            
            l_height = dfs(root.left) # recurse through left subtree to get it's height
            r_height = dfs(root.right) # recurse through right subtree to get it's height

            if abs(l_height - r_height) > 1: # if diff in height of the two subtrees differs > 1 , change global var to false
                self.is_balanced = False
            
            return 1 + max(l_height, r_height) # return max height at curr level
        dfs(root) # run the helper dfs func 
        return self.is_balanced # return the global var (changed through dfs if not balanced)