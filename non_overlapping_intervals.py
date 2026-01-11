class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals in ascending order by start time
        # have a prev interval to eval with curr interval
        # if start of curr is >= end time of prev then its NOT overlapping so just make curr prev for next iteration
        # otherwise we remove the one with the later end time and set the appropriate prev for next iteration (add 1 to count of removals)

        # time: O(nlogn)
        # space: O(1)
        
        count = 0
        intervals = sorted(intervals, key=lambda x:x[0], reverse=False)
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] >= prev[1]:
                prev = interval
            else:
                if prev[1] > interval[1]:
                    prev = interval
                count += 1 
        return count 