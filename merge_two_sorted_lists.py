# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy node for returning the new head at end
        head = dummy # head node used to attach nodes to its end
        while list1 and list2: # keep going until one list is empty
            val_1 = list1.val # get curr node value from list1
            val_2 = list2.val # get curr node value from list2
            
            # add the new list the node with the smaller value
            if val_1 < val_2:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        # case if list1 is not empty but list2 is 
        while list1: # keep adding all nodes from list1 to new list
            head.next = list1
            list1 = list1.next
            head = head.next
        while list2: # same case as above but for list2
            head.next = list2
            list2 = list2.next
            head = head.next
        return dummy.next  # return the head of the new list