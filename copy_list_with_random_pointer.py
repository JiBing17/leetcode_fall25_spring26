"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy = head # pointer to head
        old_to_new = {None:None} # mapping from old nodes to new nodes

        while dummy: # go through each node in linked list to populate the mapping
            old_to_new[dummy] = Node(dummy.val) # create new node and store in dict where key is old node and val is new node
            dummy = dummy.next # next node
        dummy = head # reset pointer back to head 

        while dummy: # go through one more time to now fix the pointers
            # update next pointer to new next node after all new node creation is done
            old_to_new[dummy].next = old_to_new[dummy.next] 
            # update next pointer to new random node after all new node creation is done
            old_to_new[dummy].random = old_to_new[dummy.random] 
            dummy = dummy.next # next node
        return old_to_new[head] # return head of the deep copy linked list