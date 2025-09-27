class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)] # init dp arr to be bool if we can partition string from i to n using the dict
        dp[-1] = True # base case : can partition empty string

        for i in range(len(dp) - 1, -1, -1): # from right to left 
            for word in wordDict: # for each word 
                if i + len(word) <= len(s) and s[i:i+len(word)] == word: # if word is substring from i 
                    dp[i] = dp[i+len(word)] # set state to state before that word if we could've fit the word before curr word
                if dp[i]: # if we could then we dont need to try other words that can mess up the bool state
                    break
        return dp[0] # return if we can parition string from first index to n using dict 