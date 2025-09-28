class Solution:
    def countSubstrings(self, s: str) -> int:

        res = [] # arr to store the palindromic substrings 

        for i in range(len(s)): # for each char in s

            l, r = i, i # make substr from curr i pos for odd len substr
            while l >= 0 and r < len(s) and s[l] == s[r]: # valid substr that is a palindrome
                res.append(s[l:r+1]) # add substring to res arr
                # expand curr string for next potential match 
                l -=1 
                r += 1 

            l, r = i, i+1 # make substrs from curr i pos for even length substrings
            while l >= 0 and r < len(s) and s[l] == s[r]: # valid palindrome
                res.append(s[l:r+1]) # add to res arr
                # expand curr string for next potential match 
                l -=1
                r += 1 

        return len(res) # return num of substrings that we captured that was a palindrome