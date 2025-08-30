class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        
        my_deque = deque() # tell us most recent and least recent elements
        seen = set() # unique values seen in window so far 
        longest_seen = 1 # length of longest substring seen overall 

        l,r = 0,0 # init window size 

        while r < len(s): # evaluate each char in s until after last char 

            char = s[r] # get current char 
            while char in seen: # if we seen it in the window, decrease elements from back of window
                val = my_deque.popleft() # remove least recent element from window
                seen.remove(val) # remove that from seen too
                l += 1 # decrease window size

            seen.add(char) # finally add curr to seen
            my_deque.append(char) # add to window 
            longest_seen = max(longest_seen, r - l + 1) # see if we have a new longest length after
            r+=1 # increase window size for next iteration

        return longest_seen # return longest seen overall at end after evaluating everything