class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # sort intervals by start time
        # sort queries in ascending order so we can safely throw out intervals in the min heap effectively if their end time < curr query num since query num will always get bigger
        # use min heap that sorts based on size (also keep ending time to check if curr query num is within bounds)
        # init res arr to all -1s.
        # keep adding to heap as long as start time <= num 
        # pop from when end time < num (num not within range of that query and queries after)
        # finally add the size of the first item in heap (if one exist) which would indicate the SMALLEST size interval that includes the num where start time <= num <= end time


        intervals = sorted(intervals, key=lambda x:x[0], reverse=False)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        q = []
        res = [-1 for i in range(len(queries))]
        i = 0

        for query_num, index in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= query_num:
                    size = intervals[i][1] - intervals[i][0] + 1
                    heapq.heappush(q, (size, intervals[i][1]))
                    i += 1

            while q and q[0][1] < query_num:
                heapq.heappop(q)
            if q:
                res[index] = q[0][0]
        return res

        # brute force approach
        # for every query, check each interval to see if query num is in there, if so keep track of min interval size of ALL intervals that are valid 
        
        intervals = sorted(intervals, key=lambda x: x[1] - x[0] + 1)
        res = []

        for num in queries:
            added = 0
            for interval in intervals:
                if interval[0] <= num <= interval[1]:
                    res.append(interval[1] - interval[0] + 1)
                    added = 1 
                    break
            if not added:
                res.append(-1)
        
        return res