# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # tail of reverse list 
        while head: # move to each node until end
            next_node = head.next # save ref of next node of curr node
            head.next = prev # redirect next pointer to point to node behind curr node (null on first iteration)
            prev = head # have prev be the curr node for next iteration
            head = next_node # move curr to next node in regular linked list
        return prev # return the new head of reversed linked list