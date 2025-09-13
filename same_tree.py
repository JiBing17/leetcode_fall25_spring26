# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_same = True # global var to indicate if the two trees are the same or not

        def dfs(p, q): # helper dfs used on the two trees to potentially modify the global bool 
            if not p and q: # no node on p tree but node on q - not same 
                self.is_same = False
                return
            if p and not q: # node on p tree but no node on q - not same
                self.is_same = False
                return
            if not p and not q: # reached leaf node on both
                return

            if p.val != q.val: # otherwise, both nodes are available so we compare its values - case if not same
                self.is_same = False
                return

            dfs(p.left, q.left) # recursively call this on both trees' left subtree
            dfs(p.right, q.right) # recursively call this on both trees' right subtree

        dfs(p,q) # start the dfs helper func 
        return self.is_same # return the global bool to see if same after the dfs run on the two trees