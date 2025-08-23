class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) # size of array
        seen = {} # hashmap where key is the number seen and value is what indice it was seen at
        for i in range(n): # iterate through each number in nums
            diff = target - nums[i] # find missing value to make up target if we are using nums[i]
            if diff in seen: # see if we have already seen this value in hashmap
                return [i, seen[diff]] # if so return the missing value's indice and current indice of num
            seen[nums[i]] = i # otherwise we just store the current num's indice in the hashmap and continue