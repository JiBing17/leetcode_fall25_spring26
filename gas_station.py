class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # make another arr with gas - cost for ALL indicees
        # if gas[i] < cost[i], then its impossbile to even start from there
            # [1,2,3,4,5] - [3,4,5,1,2]
            # [-2, -2, -2, 3, 3]

        n = len(gas) # get num of stations
        diff = []
        for i in range(n): # make diff arr
            diff.append(gas[i] - cost[i])
        
        if sum(diff) < 0: # impossible to make a round trip case
            return -1
            
        res = 0
        fuel = 0 # curr fuel in tank
        for i in range(n): # for each num in diff
            fuel += diff[i] # add the net val 

            if fuel < 0: # if we can't make it to next station 
                fuel = 0 # reset to try next station
                res = i+1 # set answer to next station since there is bound to be a sol
        return res # return the answer at end of for loop

        # brute force, try every station and return -1 if none works or the index that actually makes this work
        # time : O(n^2)

        def isValid(i):
            fuel = 0
            origin = i 
            fuel += gas[i]
            fuel -= cost[i]
            i = (i + 1) % len(gas)
            while i != origin and fuel >= 0:
                fuel += gas[i]  
                fuel -= cost[i]
                i = (i + 1) % len(gas)
            if fuel < 0:
                return False
            return True

        for i in range(len(gas)):
            if isValid(i):
                return i
        return -1