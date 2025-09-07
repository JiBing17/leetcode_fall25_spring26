# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head # fast and slow pointer to find node in middle to split list in half

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head_2 = slow.next  # new head of 2nd half of list
        slow.next = None # cut list in half by adding None val to end first half of list

        prev = None # reverse second half of list to get nth node as head
        while head_2: 
            next_node = head_2.next
            head_2.next = prev
            prev = head_2
            head_2 = next_node
        
        while head and prev: # prev node is head of 2nd reverse half list 
            next_node_1 = head.next # save ref to next nodes of the 2 lists
            next_node_2 = prev.next

            head.next = prev  # half next pointer of curr node in first half point to curr node in second half
            prev.next = next_node_1 # have curr node in second half's next pointer point to next node of first list

            head = next_node_1 # move to next node in both lists to repeat process
            prev = next_node_2