class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # impossible cases:
            # num of cards % groupSize != 0
        # keep track of min val in hand 
        # makee group starting with min val that is size groupSize
        # update min val after 
        # have hash map to map num to occurences
        # return False once a concecutve num no longer exists when making a group

        n = len(hand)
        if n % groupSize != 0: # impossible to make into equal group size case
            return False

        mapping = {} # hash map of card values to their counts 
        for num in hand:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        
        min_q = list(mapping.keys()) # min heap for keeping track of min card value in hand so far 
        heapq.heapify(min_q)

        while min_q: # while there are still cards in hand
            min_num = min_q[0]  # find min val 
            for i in range(min_num, min_num + groupSize): # find the concecutive nums starting from min num to make group size
                if i not in mapping: # if we dont have card value, then can't make 
                    return False

                mapping[i] -= 1 # otherwise update count (using card in this group)
                if mapping[i] == 0: # if no more of that val (val is NOT the starting card)
                    if i != min_q[0]: # and we still need to eventually start another group wiht the same min val then we can make the concecutive group again even tho we have to
                        return False  # retrun False in that case
                    heapq.heappop(min_q) # otherwie that val wa the min val , so we just update to new min val and continue
        return True # return True once we deal all the cards and was a success 

