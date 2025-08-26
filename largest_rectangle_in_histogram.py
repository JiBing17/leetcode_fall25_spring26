class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0 # max area seen overall
        stack = [] # stack used to store height and pos of most recent bar
        for i, bar in enumerate(heights): # go through each height + index value
            start = i # starting position of bar - default = i

            # found shorter bar than most recent, so keep removing prevs but updating calc each time
            while stack and stack[-1][1] > bar: 
                arr = stack.pop() # get info on most recent bar - height and index/pos
                start = arr[0] # start pos of most recent bar
                area = (i - arr[0]) * arr[1] # area of most recent bar if we include curr bar with it
                max_area = max(max_area, area) # find overall max after calc 
            stack.append([start,bar]) # add curr bar onto stack (start pos might've changed if we found smaller bar than prev)

        while stack: # at end, still need to account for bars still in stack if any
            arr = stack.pop() 
            w = len(heights) - arr[0]
            h = arr[1]
            max_area = max(max_area, w * h) # update max_area if appropriate
        
        return max_area # return max_area after finishing all possible computations