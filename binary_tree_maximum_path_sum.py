# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if no curr node, return 0 
# if curr node is NOT postive, then max path sum is max(left_tree, right_tree)
# if positive, max path sum is curr val + max(left, right, left + right )

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float('-inf') # global var to keep track of max path sum found so far
        def dfs(node): # traverse tree with DFS
            if not node: # no node, return 0 - base
                return 0

            left_sum = max(0, dfs(node.left)) # max path sum going down from left child
            right_sum = max(0, dfs(node.right)) # max path sum going down from right child

            self.res = max(self.res, node.val + left_sum + right_sum) # get path from left using curr node as bridge to right path and update overall if needed
            
            return node.val + max(left_sum, right_sum) # update max path going down from curr node

        dfs(root) # run DFS
        return self.res # return max path sum overall
