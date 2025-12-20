class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums 
        heapq.heapify(q) # make min heap from input arr

        while len(q) > k: # remove until heap only contains the top k elements
            heapq.heappop(q)
        return q[0] # return the kth largest element