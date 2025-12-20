class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [] # arr used for heap
        res = [] # res array to return
        for arr in points: # for each x,y pair
            dis = math.sqrt(((0-arr[0])**2) + ((0-arr[1])**2)) # find dis
            q.append([dis, arr]) # add dis with it's respective points that make it up to arr
        heapq.heapify(q) # make arr into min heap

        counter = 0 # used to keep track of how many elements to pop
        while q: # while there are still items
            if counter == k: # if we popped k items already 
                break # stop
            pair = heapq.heappop(q) # pop from q
            res.append(pair[1]) # add the x,y pair into res
            counter += 1 # update counter of total items we popped so far

        return res # return res at end