# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # global var to keep track of max diameter seen 

        def dfs(root): # helper function to find height of subtrees and use it to compute diameter
            if not root:
                return 0

            r_height = dfs(root.right) # right subtree height
            l_height = dfs(root.left) # left subtree height

            self.res = max(self.res, r_height + l_height) # potentially update diameter by adding both subtree's height
            return 1 + max(r_height, l_height) # calculate height of curr node by taking max height of its subtrees + curr node


        dfs(root) # run the dfs helper function to update res (max diameter seen)
        return self.res # return the updates global res