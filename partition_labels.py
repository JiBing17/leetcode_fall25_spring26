class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # greedy approach - cut the partition as early as possbile knowing the earliest ending of all the chars of that partition 

        mapping = {} # map char to their last occurence in the string s
        for i, char in enumerate(s): # populate mapping 
            if char not in mapping:
                mapping[char] = i
            mapping[char] = i
        
        res = [] # res arr to store size of partition 
        max_reach = 0 # end of curr partition index
        size = 0 # size of curr partition
        for i, char in enumerate(s): # for each char in s 
            last_index = mapping[char] # find last occurence 
            max_reach = max(max_reach, last_index) # expand earliest we can end partition based of chars seen in current partition so far
            size += 1 # include curr char in partition

            if i == max_reach: # if every char so far seen doesn't appear later than curr pos, end the partition imediately
                res.append(size) # update res arr
                size = 0 # reset size for next partition size 
        return res # return res arr at end
            