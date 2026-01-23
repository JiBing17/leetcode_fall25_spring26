class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # time : O(2^n) # make branch out 2 ways on each call will max dept is n
        # space : O(n) with only options arr + call stk of size n
        # with res arr its O(C(n,k)* k)

        self.options = [] # store the possible options of nums to pick from based on n
        self.res = [] # res arr to return 
        

        for i in range(1, n+1): # populate options arr from 1 to n+1
            self.options.append(i)


        n = len(self.options) # get total num of elements in options arr
        def dfs(i, size, path): # dfs to find all possbile ways to choose k nums given n options
            
            if size == k: # if we have k numbers from curr path 
                self.res.append(path.copy())  # add numbers to res arr and return
                return    
            if i == n: # if we exhausted our options and dotn have k nums, not valid path - return
                return
            
            curr_num = self.options[i] # otherwise look at curr num 
            path.append(curr_num) # run path where we pick it 
            dfs(i+1, size + 1, path)
            path.pop() # run another where we don't pick it
            dfs(i+1, size, path)
        dfs(0,0, []) # run dfs looking at first num with empty path intially
        return self.res # return the populated res arr at end