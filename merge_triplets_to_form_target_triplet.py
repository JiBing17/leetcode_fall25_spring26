class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        seen = {} # hash map to map nums seen in 1st, 2nd, and 3rd col 
        seen[0] = set()
        seen[1] = set()
        seen[2] = set()
        
        # for each triplet 
        for arr in triplets:
            if arr[0] > target[0] or arr[1] > target[1] or arr[2] > target[2]: # its a bad triplet since at least 1 value of a column is > value in target of same col
                continue
            else:  
                for i in range(len(arr)): # otherwise add nums in triplet to correct map
                    seen[i].add(arr[i])
                
        
        # check if all nums in target triplet is also contained in all the good triplets 
        for i in range(3): 
            if target[i] not in seen[i]: # if no good triplet has that num in col i, then its impossbile to make
                return False
        return True # otherwise all 3 nums are seen within their respective col within all the other good triplets and therefore it is possbile to do operation to make target triplet                        