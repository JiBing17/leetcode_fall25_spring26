class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        valid_nums = set(nums) # add to set for quick lookup and removes duplicate values 
        longest_seen = 0 # longest seen so far in the current sequence
        longest_overall = 0 # longest seen over all the sequences

        for num in valid_nums: # iterate through each value in set
            longest_seen = 0 # reset longest seen since we are in new sequence
            if num + 1 in valid_nums: # if we can start with a num to right of current one, dont point in calculating this one
                continue
            while num in valid_nums: # else we add to longest seen, and keep going down by subtracting 
                num -= 1
                longest_seen +=1

            # update once we finish current sequence and potentially update overall
            longest_overall = max(longest_overall, longest_seen) 

        return longest_overall # return overall longest sequence    