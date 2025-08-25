class Solution:
    def trap(self, height: List[int]) -> int:

        water_trapped = 0 # intialize var to store total water trapped 
        l,r = 0, len(height) - 1 # intialize left and right pointers to start and end of array 
        maxL = height[l] # initialize longest bar seen so far going from left to right
        maxR = height[r] # initialize longest bar seen so far going from right to left 

        while l < r: # keep going until the two pointers cross / touch each other
            if maxL < maxR: # left bar is smaller than right bar - we do calculation with left bar
                l += 1 # move to left for next iteration since we did the calc here
                water = maxL - height[l] # find water trapped to the right of the left bar
                if water > 0: # if there is actually water (bar to right of left bar is shorter) 
                    water_trapped += water # add to total water
                maxL = max(maxL, height[l]) # update longest left bar seen so far if applicable (will only change if water < 0)

            else: # same concept for right bar case fi it's the shortest bar between the 2
                r -= 1
                water = maxR - height[r]
                if water > 0:
                    water_trapped += water
                maxR = max(maxR, height[r])

        return water_trapped # at end, return total water trappe