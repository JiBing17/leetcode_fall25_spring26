class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.res = [] # res arr to return at end
        self.part = [] # arr used for each branches partion choices
        def isPali(word): # helper to check if word is palindrome or not
            l,r = 0, len(word) - 1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True 

        def dfs(i): # helper dfs to compute different partitions to find valid ones to store in res arr
            if i == len(s): # reached end of string add all the valid partition strings for this branch onto res arr
                self.res.append(self.part.copy())
                return
            
            for j in range(i,len(s)): # expand word starting from index i to j  
                curr_string = s[i:j+1] # get substr
                if isPali(curr_string): # check if valid palindrome
                    self.part.append(curr_string) # if so, add to sub arr
                    dfs(j+1) # recursively call on the left over string for any other valid palindromes with the leftover str
                    self.part.pop() # backtrack by removing our partition choice for next loop
        dfs(0) # start at index 0 of string 
        return self.res # return the res arr at end of dfs call