class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # merge interval logic:
        # have a prev interval to compare with curr
        # if no overlap, add prev to list
        # if overlap, "merge" the two and make that prev for next iteration

        # time : O(n)
        # space: O(1) if not counting res arr to return

        
        res = [] # res arr to return the updated intervals at end after merging
        prev = None # prev interval before curr one to check for merge or not
        intervals = sorted(intervals, key=lambda x: x[0], reverse=False) # first sort intervals in ascending order based on start time
        for interval in intervals: # for each interval 
            if not prev: # always assign prev to first interval
                prev  = interval
            else: # otherwise 
                if prev[1] < interval[0]: # prev interval's end time doesn't overlap with curr's start time 
                    res.append(prev) # add prev interval block to res
                    prev = interval # redefine prev block to curr block for next iteration
                else:
                    prev = [min(prev[0], interval[0]), max(prev[1], interval[1])] # otherwise if prev and curr intervals overlap, merge them and that will be prev interval for next iteration
        if prev:  
            res.append(prev) # at end, there will be no curr, so just add the prev interval to the end, ending the algorithm 
        return res # return the updated intervals arr