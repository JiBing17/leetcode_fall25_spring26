# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] # stack to keep track of smallest node vals on top using in order traversal
        n = 0  
        
        while stack or root: # while stack not empty or there is a node to process ...
            while root: # keep adding to stack moving left 
                stack.append(root)
                root = root.left
            root  = stack.pop() # pop leftmost node  - smallest 
            n += 1 # update the number of the smallest node so far
            if n == k: # if it matches k, then we found the value of the kth smallest node
                return root.val
                
            root = root.right # explore the curr node's right subtree and repeat the inorder traversal