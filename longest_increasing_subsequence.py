class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))] # init dp arr where ith pos means the longest subsequence ending at the ith element
 
        for i in range(1, len(nums)): # populate the rest of the dp arr by going through each element i 
            for j in range(0, i): # for each element behind i lets call j 
                if nums[i] > nums[j]: # if element i > element j , then we can have a potentially longer sequence
                    # longest can it's current longest or longest sqeunce ending at j + 1 for element i 
                    dp[i] = max(dp[i], dp[j] + 1) 

        return max(dp) # return max of dp since longest sequence can end up on any of the elements in the arr 