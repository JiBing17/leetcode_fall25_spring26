class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = [] # arr of updated intervals after insertion to return

        for i, interval in enumerate(intervals): # for each interval
            if newInterval[1] < interval[0]: # if end time of new is behind start of curr
                res.append(newInterval) # add new interval first (separate interval)
                return res + intervals[i:] # followed by rest of the intervals from curr and after
            elif newInterval[0] > interval[1]: # if start of new interval is after the end of curr one
                res.append(interval) # add curr one first (separate interval) but leave out rest since it's possbile for new to merge with the following intervals
            else: # otherwise it's overlapping between curr one (maybe more too) so merge by taking the earlier of the two start time for head and later of the two end time for tail 
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            # note we do NOT add new interval after merge since there could be more overlap with the following intervals after curr
        res.append(newInterval) # so only append the merged interval at end
        return res # return the new updated res arr of intervals after the add