class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 1: # case if s is of size 1
            return 1

        seen = {} # map of letter to count in current window 
        l = 0 # left pointer init 
        longest_seen = 1 # min longest seen overall init
        longest_so_far = 1 # min longest seen so far in window

        for r in range(len(s)): # expand window - move right pointer right 
            char = s[r] # get most recent char

            if char not in seen: # update mapping
                seen[char] = 0
            seen[char] += 1

            longest_so_far = max(longest_so_far, seen[char]) # update longest repeated char after updating mapping

            while (r - l + 1) - longest_so_far > k: # if don't have enough replacements given window size - longest length of repeated char without replacement 
                char_removed = s[l] # remove from end of window
                seen[char_removed] -= 1 # update mapping of that char
                l += 1 # reduce window size

            longest_seen = max(longest_seen, r - l + 1) # valid now, so update longest overall with curr window size
        return longest_seen # return overall longest repeated length 