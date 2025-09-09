class Solution:
    def findDuplicate(self, nums: List[int]) -> int: # treat array with val and index as linked list val and next pointer 

        fast,slow = 0,0 # init fast and slow pointer 
        while True:
            fast = nums[nums[fast]] # move 2 "nodes" ahead
            slow = nums[slow] # move 1 "node" ahead

            if fast == slow: # find start of cycle 
                break
        slow_2 = 0

        while True: # find the dup in the cycle, advancing 1 by 1
            slow = nums[slow]
            slow_2 = nums[slow_2]

            if slow == slow_2:
                return slow 
        