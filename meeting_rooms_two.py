"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# time : O(nlogn) where n is the total num of intervals given to us 
# space: O(n) 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals) # define total num of intervals
        start_times = [] # arr to store start times in ascending order
        end_times = [] # arr to store end times in ascending order

        for interval in intervals: # populate the 2 arrs
            start_times.append(interval.start)
            end_times.append(interval.end)
        
        # sort the 2 populated arrs
        start_times.sort() 
        end_times.sort()

        # indices used for the 2 arrs
        i = 0
        j = 0

        count = 0 # total num of rooms booked currently
        res = 0 # overall max room seen throughout the eval

        while i < n: # while we still have meetings to start
            if start_times[i] < end_times[j]: # if earliest meeting starts before the curr earliest meeting's end time
                count += 1 # then we need to book an addition room
                i += 1  # look at next earliest meeting start time for next computation
            else:
                count -= 1 # otherwise we can free up the space after earliest meeting end time before reusing it for the next earliest meeting 
                j+=1 
            res = max(res, count) # find the max room used at any moment of time during this process
        return res # reurn overall max rooms used at end
