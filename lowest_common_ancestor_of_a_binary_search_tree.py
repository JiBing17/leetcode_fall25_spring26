# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: # leaf node, just return 
            return 
        if root.val < p.val and root.val < q.val: # lca could only be on the right subtree due to bst
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val: # lca could only be a the left subtree due to bst
            return self.lowestCommonAncestor(root.left, p, q) 
        return root # lca can only be curr ancestor since p and q are in different subtrees due to bst