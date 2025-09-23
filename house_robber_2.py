class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: # only 1 house - return cost after robbing that 1 house
            return nums[0]  

        if len(nums) == 2: # only 2 houses - return max between the 2 (rob the house with more money)
            return max(nums[0], nums[1])

        # new nums arr without last house - used for computing max amount if we choose not to consider last house
        nums1 = nums[:-1]

        # new nums arr without first house - used for computing max amount if we choose not to consider last house
        nums2 = nums[1:]

        # init 2 dp arrs for computing the 2 cases 
        dp1 = [0 for i in range(len(nums1))] 
        dp2 = [0 for i in range(len(nums2))]

        dp1[0] = nums1[0] # base cases for dp1 - not including last house
        dp1[1] = max(nums1[0], nums1[1])

        dp2[0] = nums2[0] # base cases for dp2 - not including first house
        dp2[1] = max(nums2[0], nums2[1])

        for i in range(2, len(nums1)): # regular house robber problem with nums1
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums1[i])
       
        for i in range(2,len(nums2)): # regular house robber problem with nums2
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums2[i])
       
        # return the max between the 2 cases to get overall max of the two choices
        return max(dp1[len(nums1) - 1], dp2[len(nums2) - 1]) 
