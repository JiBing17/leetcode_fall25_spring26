class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # can't sort array due to wanting sub array from orignal input array
        # we keep expanding sub array and update overall sum at each point, if adding nums[i] to curr sum is worst than just starting at nums[i], then restart subarray at nums[i] 
        # then we can start over and repeat until end

        overall_max = float('-inf') # init to -inf 
        curr_sum = float('-inf') # init to -inf

        for i in range(len(nums)): # for each num 

            curr_sum = max(nums[i], curr_sum + nums[i]) # choose to add to curr running sum or restart with that
            overall_max = max(overall_max, curr_sum) # update overall sum from all subarrays so far

        return overall_max # return answer