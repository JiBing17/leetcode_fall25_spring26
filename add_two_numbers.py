# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        remainder = 0 # keep track of remainder from prev computation 
        dummy = ListNode() # dummy node to return head of new linked list at end
        head = dummy # head var used ot iterate through the new linked list 

        while l1 and l2:
            val_1 = l1.val # get val of curr node of list 1
            val_2 = l2.val # get val of curr node of list 2
            computed = val_1 + val_2 + remainder # compute sum
            if computed > 9: # case if remainder, save it and only use the last digit 
                remainder = 1 
                computed -= 10
            else: # otherwise no remainder so set remainder to 0 for next iteration
                remainder = 0
            computed_node = ListNode(computed) # create new node for the sum val
            head.next = computed_node # link it to new linked list
            head = computed_node # update ref to last node in new linked list
            l1 = l1.next # go to next node for linked list 1
            l2 = l2.next # go to next node for linked list 2
        
        while l1: # keep adding nodes if l1 is not empty 
            val_1 = l1.val 
            computed = val_1 + remainder 
            if computed > 9: # case if remainder, save it and only use the last digit 
                remainder = 1 
                computed -= 10
            else: # otherwise no remainder so set remainder to 0 for next iteration
                remainder = 0
            computed_node = ListNode(computed) # create new node for the sum val
            head.next = computed_node # link it to new linked list
            head = computed_node # update ref to last node in new linked list
            l1 = l1.next # go to next node for linked list 1

        while l2: # keep adding nodes if l2 is not empty 
            val_2 = l2.val 
            computed = val_2 + remainder 
            if computed > 9: # case if remainder, save it and only use the last digit 
                remainder = 1 
                computed -= 10
            else: # otherwise no remainder so set remainder to 0 for next iteration
                remainder = 0
            computed_node = ListNode(computed) # create new node for the sum val
            head.next = computed_node # link it to new linked list
            head = computed_node # update ref to last node in new linked list
            l2 = l2.next # go to next node for linked list 2

        if remainder == 1: # end case where we have remainder at end 
            head.next = ListNode(1)  # add extra node with val 1 
        return dummy.next # return head of new linked list