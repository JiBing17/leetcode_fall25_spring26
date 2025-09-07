# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# intuition since fast moves twice as fast as slow, if there is a cycle then it will eventually catch up to slow 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        fast, slow = head, head # init fast and slow pointers 
        while fast and fast.next: # while fast can move up to the next two nodes
            fast = fast.next.next # advance fast two nodes
            slow = slow.next # advance slow one node
            if slow == fast: # if fast somehow catches back to slow pointer, then there is a cycle
                return True
        return False # fast node exited list, no cycle then