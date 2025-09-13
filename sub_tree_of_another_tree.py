# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root, subRoot): # helper to check if these trees are the same or not
            if not root and not subRoot: # both reached leaf nodes return true
                return True
            # not leaf nodes and values are the same, recursive on subtrees to find if they are both the same too - true if so
            if root and subRoot and root.val == subRoot.val: 
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
                
            return False # other wise not same tree

        if not subRoot: # root is subTree of empty subRoot
            return True
        if not root: # can't have subtree in empty tree
            return False
        
        if isSameTree(root, subRoot): # check if these two trees are the same 
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # try testing if left subtree or right subtree is a subtree of subRoot next 