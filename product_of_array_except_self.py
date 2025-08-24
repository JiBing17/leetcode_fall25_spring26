# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # size of array 
        res = [1 for i in range(n)] # initial resulting array to all 1s 
        prefix = 1 # product of all elements to the left of current element
        posfix = 1 # product of all elements to the right of current element

        for i in range(n): # from left to right
            res[i] = prefix # populate res array with prefix 
            prefix *= nums[i] # update prefix 

        for i in range(n-1, -1, -1): # from right to left
            res[i] *= posfix # update res by including product of all elements from the right side as well (left already done)
            posfix *= nums[i] # update postfix

        return res # return the updated res array at end