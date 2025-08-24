class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers) - 1 # intialize left and right pointer to point to first and last element of numbers array

        while l < r: # while right pointer didn't pass left pointer
            value = numbers[l] + numbers[r] # sum up the first two values that the l and r pointer is pointing at 
            if value == target: # if we found a match
                return[l+1, r+1] # return the indices of the two values +1 for 1 indexed
            elif value > target: # if sum is too big, we can reduce the value of sum by moving r pointer left since sorted
                r -= 1 
            else: # if sum is too small, we can increase the value of sum by moving l pointer to the right since sorter
                l += 1  