class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1 # initialize left and right pointers at both ends of array
        max_area_seen = 0 # intialize max area seen overall
        while l < r: # while the two pointers haven't passed / touch each other yet
            width = r - l # find width (distance between the 2 pointers)
            curr_area = 0 # intialize current area for this iteration
            if height[l] > height[r]: # r points to the shorter vertical line
                curr_area = width * height[r] # calculate current area based on shorter line as height
                r -= 1 # next iteration move right pointer left (prevent skips if we move shorter line)
            else:
                curr_area = width * height[l] # left pointer points to shorter vertical line, same concept
                l += 1 
            max_area_seen = max(max_area_seen, curr_area) # update overall maximum area seen if applicable
        return max_area_seen # return overall max at the end