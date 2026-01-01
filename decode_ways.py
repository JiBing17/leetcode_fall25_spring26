class Solution:
    def numDecodings(self, s: str) -> int:
        
        # dp[i] = total num of ways to decode digit starting from i
        n = len(s) # get num of digits 
        dp = [0 for i in range(n+1)] # make dp arr init to 0s
        dp[n] = 1 # num way to decode empty string
        for i in range(n-1, -1,-1): # from right to left 
            if s[i] == "0": # if starting is 0, then not possible to decode
                dp[i] = 0 # set to 0 
                continue # next iteration 

            dp[i] = dp[i+1] # otherwise we can decode it the same way we decoded the digit starting at i+1 since a way is just decoding 1 by 1

            if i + 2 <= n and 1 <= int(s[i:i+2]) <= 26: # if digit starting at i can expand to right to include 2 digits and its valid
                dp[i] += dp[i+2] # add to it num of way to decode num startign from i+2 (i and i+1 acts as one letter)
        return dp[0] # return num of ways to decode from begining of string s