class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # array to return 
        nums.sort() # sort array for two pointer method 
        n = len(nums) # size of array
        for i in range(n-2): # from left to right excluding last two elements (needed for two pointers)
            if i > 0 and nums[i - 1] == nums[i]: # can't use name value as last iteration, skip
                continue

            l,r = i+1,n-1 # intialize two pointers where l is value to right of the ith value and r points to last element
            missing_val = 0 - nums[i] # determine what value we are missing in order to add to 0 if we use ith element
            while l < r: # twp pointer method to find next two values
                if nums[l] + nums[r] == missing_val: 

                    # if the r and l pointers point to values that match missing val, add to answer, update both r and 
                    # l pointers approriately, skipping values that are the same as the one we used for answer
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]: # skip case for l pointer
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: # skip case for r pointer
                        r -= 1
                # case if doesnt fit missing val and sum is smaller, move l pointer right for a bigger val
                elif nums[l] + nums[r] < missing_val: 
                    l += 1
                # case if doesnt fit missing val and sum is bigger, move r pointer left for a smaller val
                else:
                    r -= 1   
    
        return res # return res at end          