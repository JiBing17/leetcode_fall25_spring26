class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums # set var for passed in array 
        self.n_largest = k # set var for passed in k val
        heapq.heapify(self.arr) # make heap from array 


    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val) # add toheap (self.arr) with val
        while self.arr and len(self.arr) > self.n_largest: # keep popping until only k elements left (since min heap by default, k would be the k biggest elements left)
            heapq.heappop(self.arr)
        return self.arr[0] # return the kth biggest element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)