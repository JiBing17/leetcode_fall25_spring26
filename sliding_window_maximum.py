class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # array to store result
        window = deque() # deque data structure used to remove from left and right ends as well as add to right end (decreasing deque) - intuition : top value at left end and store indices instead of val to keep additional track of window position too 
        l = 0 # left index of left end of window 
        for r in range(len(nums)): # right end of window increasing 1 at a time


            while window and nums[r] >= nums[window[-1]]: # keep popping from top of deque if curr val is >= (decreasing dequeue) 
                window.pop() 
            window.append(r) # curr val is now smaller then top most element, add to top now (add index to keep track of window pos and what vals to keep)

            if r - l + 1 == k: # valid window
                res.append(nums[window[0]]) # add left most element of deque (should cotain biggest val)
                l+= 1 # decrease window 
            

            if window and l > window[0]: # remove val from deque if window no longer covers that index
                window.popleft()

        return res # return populated array at end 