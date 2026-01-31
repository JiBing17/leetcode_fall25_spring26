class MedianFinder:

    def __init__(self):
        self.min_heap = [] # right half of the array of nums that will be added
        self.max_heap = [] # left half of the array of nums that will be added

        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        
    # time : O(m*logn) where m is amount of addNum calls and n is num of elements added 
    # time : O(m) for find median calls where we call it m times (constant time func)

    # space : O(n) where n is total of elements added for heap


    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, -1 * num) # always add to left half first

        if self.max_heap and self.min_heap and -1 * self.max_heap[0] > self.min_heap[0]: # if there is a state inbalanced adjust the elements in heaps to maintain state
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        if len(self.max_heap) > len(self.min_heap) + 1: # if size is also diff by more than 1 adjust as well, we need both to have about half for find median to work 
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > len(self.max_heap) + 1: # same for other case 
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)

    def findMedian(self) -> float: # find in constant time based on the two heaps and if total elements n is even or odd
        n = len(self.max_heap) + len(self.min_heap) 
        if n % 2 == 0:
            return (((-1 * self.max_heap[0]) + self.min_heap[0]) / 2)
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -1 * self.max_heap[0]
            return self.min_heap[0]
    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()