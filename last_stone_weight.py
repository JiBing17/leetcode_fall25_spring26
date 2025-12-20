class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [] # define arr to make into heap
        for stone in stones: # convert stone weight to negative version for Python heap - we want max heap but python only has min heap (*-1 will treat it like max heap)
            q.append(stone * -1)
        heapq.heapify(q) # make array into heeap

        while len(q) > 1: # while there is more than 1 item in heap
            stone_one = heapq.heappop(q) * -1 # pop first heaviest stone
            stone_two = heapq.heappop(q) * -1 # pop second heaviest stone

            if stone_one > stone_two: # if 1st stone is heavier
                heapq.heappush(q, (stone_one - stone_two) * -1) # add diff between 1 and 2 back into heap 
            elif stone_one < stone_two: # otherwise its diff between 2 and 1 if 2 is heavier
                heapq.heappush(q, (stone_two - stone_one) * -1)
            # if same, do nothing, just remove both stones, no adding 

        if q: # if 1 stone left, return the weight of stone in heap
            return q[0] * -1
        else: # otherwise return 0 in case last 2 stones were the same 
            return 0 
