class Solution:

    def can_finish(self, piles, curr, h) -> bool: # helper function used to determine if it's possbile to finish all piles before a given hour given a passed in rate (curr var in this case)
        total_time = 0  # var used ot keep track of total hours accumulated if we eat curr bananas in h hours 
        for pile in piles:  # accumulate hours
            total_time += math.ceil(pile / curr)
        return total_time <= h # reutnr if we have finished before h hours or not 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        upper = max(piles) # define upper bound of k (max in array since that would take n (length of piles) hours to finish)
        l,r = 1, upper  # define l and r pointers as bound for k
        min_h = upper # by default min rate to finish is upper var
        while l <= r: # while we have not pass points (haven't exhausted our options)
            curr = (l + r) // 2 # find mid value (try this k value)
            finish = self.can_finish(piles, curr, h) # see if we can finish on time
            if finish: # if we can, then we have a new smaller val and adjust bounds to try a smaller val next iteration
                min_h = curr # update smallest seen
                r = curr - 1 # adjust for smaller mid val next 
            else:
                l = curr + 1 # if we can't finish adjust bounds so we have a bigger k next
        return min_h # return min k overall after while loop  