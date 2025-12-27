# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # If there are no nodes left to process, return None
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0]) # the 1st element is always the root of the tree/subtree

        # find the root position in inorder traversal
        # everything LEFT of this index belongs to the left subtree
        # everything RIGHT of this index belongs to the right subtree
        mid = inorder.index(preorder[0])

        # Build the LEFT subtree
        # preorder:
        #   skip the root (preorder[0])
        #   take the next 'mid' elements -> left subtree nodes
        # inorder:
        #   take everything BEFORE root -> left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Build the RIGHT subtree
        # preorder:
        #   remaining elements after left subtree
        # inorder:
        #   everything AFTER root
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
