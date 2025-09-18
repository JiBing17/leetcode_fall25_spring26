class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "": # empty digits case - just return empty array
            return []

        mapping = {} # dict for defining which numbers map to which letters
        mapping["2"] = "abc"
        mapping["3"] = "def"
        mapping["4"] = "ghi"
        mapping["5"] = "jkl"
        mapping["6"] = "mno"
        mapping["7"] = "pqrs"
        mapping["8"] = "tuv"
        mapping["9"] = "wxyz"

        self.res = [] # final res arr to return 

        def dfs(i, string): # dfs to explore all possible combs for eahc digit and populae res arr with it 
            if i >= len(digits): # evaluated all digits, add the curr combination string to res arr and return
                self.res.append(string)
                return
            
            curr_num = digits[i] # get curr num that we are evaluating 
            letters = mapping[curr_num] # get the corresponding letters to that number

            for char in letters: # for each of the letters of that num
                string += char # recursively call func in the case we chose that letter for this num
                dfs(i+1, string) # call func with new string and evaluate next digit
                string = string[:-1] # backstrack by removing the picked char for next recursively call in the next iteration
        dfs(0,"") # run dfs starting from first digit and an empty string
        return self.res # return the populate res arr at the end of the dfs calls