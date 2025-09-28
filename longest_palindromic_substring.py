class Solution:

    def longestPalindrome(self, s: str) -> str:
        longest = s[0] # base case longest palindrome is just the a char in the string s
        
        for i in range(len(s)): # for each char in s 

            l,r = i, i # evaluate odd substrings expanding outwards from each char at i

            # if substring is within bounds and valid, update longest seen if longer
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                if r - l + 1  > len(longest):
                    longest = s[l:r + 1]

                # expand outwards for substring to find longer possible palidnrome
                l -= 1 
                r += 1
            
            # evaluate even substrings expanding outwards from each char at i and i+1 for even 
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: # if valid sub and substring is in bound
                if r - l + 1  > len(longest): # update longest if we found longer substring
                    longest = s[l:r+1]
                # expand outwards for substring to find longer possible palidnrome
                l -= 1 
                r += 1 

        return longest # return longest substr seen after end of all computation
