class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapping = {} # hash map letter to occurrences
        q = [] # arr used for min heap
        count = 0 # total time to return
        dq = deque() # hold items that can't be considered due to interval 

        for char in tasks: # populate hashap char to occurrences 
            if char not in mapping:
                mapping[char] = 0
            mapping[char] += 1
        
        for key,value in mapping.items(): # add letter, ocurrences pair to heap (*-1 for maxHeap)
            q.append([-1*value,key])
        heapq.heapify(q)

        while q or dq: # while we have nothing to process or there is still entries waiting on interval to finish

            count += 1 # add to total time 
            if q: # if item in heap
                arr = heapq.heappop(q) # compute most frequent letters first 
                arr[0] = ((arr[0] * -1) - 1) * -1 # decrement how much letters we still need ot compute
                if arr[0] < 0: # only add back to heap if there is more
                    dq.append([arr, count + n])
                
            if dq and dq[0][1] == count: # if there are items suspended from being considered due to interval constraint and time is passed so it can be reused 
                arr = dq.popleft() # remove from this deque from FIFO order
                heapq.heappush(q, arr[0])  # add to heap again for processing
        return count # returm total time it took for everything at end

        
        return count
