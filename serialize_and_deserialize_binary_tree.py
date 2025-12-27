# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = [] # arr used ot store node vals in DFS traversal way

        def dfs(root):
            if not root: # no node
                res.append("N") # add N as null
                return # return 

            res.append(str(root.val)) # otherwise add string of that val to res

            dfs(root.left) # recurse and do same for left subtree 
            dfs(root.right) # recurse and do same for right subtree

        dfs(root) # run DFS
        return ",".join(res) # return string concatanated by "," for next func
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        arr = data.split(",") # return string to arr by splitting based off of ","
        self.i = 0 # have global index to this arr
        def dfs(): # DFS for making the tree
            if arr[self.i] == "N": # if its null, no tree is made, just skip 
                self.i += 1
                return
            
            node = TreeNode(int(arr[self.i])) # otherwise make the node
            self.i += 1 # update next entry for next node to be made
            node.left = dfs() # recurse to make left subtree
            node.right = dfs() # recurse to make right subtree 
            return node # return curr node to complete function
        return dfs() # run DFS and return the entire tree

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))