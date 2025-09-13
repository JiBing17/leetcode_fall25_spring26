# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.res = [] # res array to return 

        def dfs(root, level): # dfs helper function to populate res arr based on depth level

            if not root: # lead node just return 
                return 

            if len(self.res) == level: # add arr for populating vals in curr level
                self.res.append([])

            self.res[level].append(root.val) # add val to arr of its targeted lvl 

            dfs(root.left, level + 1) # recursively call it on left subtree updating the level var for adding to new arr 
            dfs(root.right, level + 1) # recursively call it on right subtree updating the level var for adding to new arr 

        dfs(root, 0) # run dfs to populate res arr
        return self.res # return arr after dfs call