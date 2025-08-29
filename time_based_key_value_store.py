class TimeMap:

    def __init__(self):
        self.mapping = {} # create dict for mapping key to values where values are [value, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None: # set function
        if key not in self.mapping:  # define array for that key to val map if no key yet
            self.mapping[key] = []
        self.mapping[key].append([value, timestamp]) # append to that array an array of size 2 containing [val, timestamp]



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping: # key not there yet, return emtpy string
            return ""
        arr = self.mapping[key] # access array for that key
        
        l, r = 0, len(arr) - 1 # define left and right pointers
        valid = -1 # valid index containing the most recent timestamp that satisfies the passed in timestamp
        while l <= r: # while we haven't exhausted all of our options
            mid = (l + r) // 2 # make mid pointer from l and r pointers
            if arr[mid][1] > timestamp: # since timestamps are in ascending order do binary search - case where we need a lower timestamp next iteration - look at left half
                r = mid - 1
            else: # valid case so we try to find a bigger (more recent) timestamp next iteration - look at right half
                valid = mid # update potential most recent timestamp index
                l = mid + 1 

        if valid == -1: # didn't find any timestamps that were <= timestamp var
            return "" 
        return arr[valid][0] # return the val of the most recent timestamp that suffices 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)