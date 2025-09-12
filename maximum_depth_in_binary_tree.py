# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: # leaf node case
            return 0 
        # recrusively call on left & right subtreees to get their height and 
        # take max + 1 to account for current tree for max length
        length = 1 + max (self.maxDepth(root.left), self.maxDepth(root.right)) 

        return length # return legnth of current tree