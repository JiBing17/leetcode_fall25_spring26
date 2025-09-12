# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_heap = [] # init arr for heap
        my_id = 0 
        for head in lists: # for each linked list...
                if head:
                    heapq.heappush(my_heap, (head.val, my_id, head)) # add val, id for tie breaker, and node - tuple for heap
                    my_id += 1 # next unused id
                    head = head.next # next node
            
        dummy = ListNode() # dummy node to return head
        head = dummy # pointer for adding to tail of resulting linked list

        while my_heap: # while heap not empty 
            val ,i, node = heapq.heappop(my_heap) # get smallest val, its id, and actual node 
            if node.next: # if there is a node after that one 
                heapq.heappush(my_heap, (node.next.val, my_id, node.next)) # add to heap
                my_id += 1 # update to next unused id
            head.next = node # connect node to resulting linked list
            head = head.next # update tail of resulting linked list 

            

        return dummy.next # return head of the resulting linked list 