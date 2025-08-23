class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set() # set used to keep track of what unique numbers we have seen so far 
        for num in nums: # loop through each number
            if num in seen: # case if we have already seen it 
                return True
            else: # case if its a new number, add to seen set
                seen.add(num)
        return False # went through entire array and all numbers are unique since we didn't return true 