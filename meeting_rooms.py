"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# time: O(nlogn) where n = total num of intervals given. sorting takes up majority time 
# space: O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: # trivial case
            return True

        intervals = sorted(intervals, key=lambda x:x.start, reverse=False) # sort based on starting time
        prev = intervals[0] # assign prev interval to interval with the earliest start time
        for interval in intervals[1:]: # from there and onwards
            if interval.start < prev.end: # if next interval's start is before prev's interval's end , then there is an overlap
                return False # return False in that case 
            else: # otherwise just update prev interval to curr interval for next iteration
                prev = interval
        return True # return True at end since ALL intervals given won't overlap with one another