class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dp_min = [float("inf") for i in range(len(nums))] # init dp for min product ending at ith pos 
        dp_max = [float("-inf") for i in range(len(nums))] # init dp for max product ending at the ith pos

        dp_min[0], dp_max[0] = nums[0], nums[0] # base case, set both dp arr's 1st val to first num in nums
        overall_max = nums[0] # overall max will also be first num to start
        
        for i in range(1, len(nums)): # populate the rest of the 2 dp arrs
            
            curr_val = nums[i] # curr val 
            min_sub_times_curr = dp_min[i-1] * curr_val # multiply curr with min product seen so far
            max_sub_times_curr = dp_max[i-1] * curr_val # multiply curr with max product val seen so far

            dp_min[i] = min(curr_val, min_sub_times_curr, max_sub_times_curr) # update min product seen given the computed vals
            dp_max[i] = max(curr_val, min_sub_times_curr, max_sub_times_curr) # update max product seen given the computed vals

            overall_max = max(overall_max, dp_max[i]) # update if we found a bigger product after computng dp max arr

        return overall_max # return overall max product arr seen over the entire arr
 