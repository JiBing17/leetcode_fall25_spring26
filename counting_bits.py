class Solution:
    def countBits(self, n: int) -> List[int]:

        # dp solution
        # have arr to keep track of total num of set bits seen in for curr num
        # keep track of the when the power of two numbers happen "break points where all 1s are cleared and there is only a new set bit" (1,2,4,8)
        # pattern when evaluating nums from 0 ... n where total set bits has a pattern 
        # example: 011 and 111 - these two are just 1 bit apart where we can ref num 3 given num 7 by doing 1 + dp[n-offset] (offset is 4 in this case)

        # time : O(n) # just a singular pass through the n nums
        # space: O(n) - store res

        dp = [0 for i in range(n+1)]
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

        # time : O(nlogn) n for nums to look at and we need to look at each bit (logn) for each num so n*logn
        # space: O(n) to store arr to return

        res = [] 

        for i in range(n+1): 
            num = i # num to eval 
            counter = 0 # counter for total num of set bits (1s)
            while num: # while we haven't revaluated all bits for curr num
                counter += num % 2 # get the least significant bit (0 or 1) and add to counter
                num = num // 2 # reduce num so we can see next bit after curr least significant one
            res.append(counter) # add to res arr adfter we evaluated curr num
        return res