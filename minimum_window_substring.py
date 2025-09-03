class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): # impossible for substring to happen if t > s 
            return ""

        res = "" # min string to return
        matches = 0 # number of matches to t - used for bool condition to see if we check or not
        t_map = {} # mapping for char to count of t string
        seen = {} # mapping for char to count of curr window 

        for char in t: # populate t string map
            if char not in t_map:
                t_map[char] = 0
            t_map[char] += 1
        
        l = 0 # left end of window
        for r in range(len(s)): # moving right end of window

            char = s[r] # curr char 
            if char not in seen: # populate seen map
                seen[char] = 0
            seen[char] += 1 

            if char in t_map and seen[char] == t_map[char]: # curr char is apart of t string, increment matches
                matches += 1
            
      
            
            while matches == len(t_map): # if we have a window showing a valid substring of s that all of t letters are in

                if not res or r - l + 1 < len(res): # update smallest string seen if needed
                    res = s[l:r+1] 
                    
                char_to_remove = s[l] # remove leftmost char 
                l += 1 # decrease the window size from left
                seen[char_to_remove] -= 1 # update seen map

                if char_to_remove in t_map and seen[char_to_remove] < t_map[char_to_remove]: # update matches if removing that char no longer satisfies the matches
                    matches -= 1
        return res # return min string at end