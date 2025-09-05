# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: # base case for recursion, no more node to recurse down
            return
        
        right_val = root.right # save right node val
        root.right = root.left # assign right node to left node
        root.left = right_val # assign left node to original left node

        self.invertTree(root.right) # recrusively call on the new right node
        self.invertTree(root.left) # recursively call on the new left node 
        return root # return root after all recursion
        