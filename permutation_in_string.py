class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): # no permutation possbile
            return False

        l = 0 # init left pointer for left end of window 
        seen_s1 = {} # mapping of each char and it's count for s1
        seen_s2 = {} # mapping of each char and it's count for window of s2

        for char in s1: # populate dict of s1
            if char not in seen_s1:
                seen_s1[char] = 0
            seen_s1[char] += 1 

        
        for r in range(len(s2)): # expand window to right for each char in s2
            char = s2[r] # get curr char 
            if char not in seen_s2: # update mapping 
                seen_s2[char] = 0
            seen_s2[char] += 1

            while (char not in seen_s1 and l < r) or r - l + 1 > len(s1): # reduce window if size is too big or curr char is not a included in perm of chars that make up s1 

                if s2[l] in seen_s2: # update s2 dict mapping after removing earliest seen char
                    seen_s2[s2[l]] -= 1

                    if seen_s2[s2[l]] == 0: # remove key if count of that char becomes 0 
                        del seen_s2[s2[l]]
                l += 1  # reduce window size
            if seen_s1 == seen_s2: # if at any point the dicts are the same, then we found a permutation, return true
                return True

        return False # otherwise at end we can return false, no perm was found 