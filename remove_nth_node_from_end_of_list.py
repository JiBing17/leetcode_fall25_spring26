# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head) # dummy node before head node, init front and back pointers to dummy node 
        front, back = dummy, dummy 

        for i in range(n): # make n gap between front and back pointer 
            front = front.next

        # iterate until front pointer points to last node (back pointer should be a node before target n node we want to remove now)
        while front.next: 
            front = front.next
            back = back.next

        back.next = back.next.next # remove the node ahead of backnode

        return dummy.next # return the head of the modified list