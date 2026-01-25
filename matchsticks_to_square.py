class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # time: O (4^n)
        # space: O(n) call stck size and sorting (merge sort) takees O(n) too
        remainder = sum(matchsticks) % 4 # sum is not multiple of 4, not possible
        if remainder:
            return False
        
        self.res = sum(matchsticks) // 4 # otherwise get size needed each side of square to be complete
        matchsticks.sort(reverse=True) # sort sticks in descending

        if matchsticks[0] > self.res: # if longest stick is > needed size, impossbile to make
            return False
        n = len(matchsticks)

        def dfs(i, square):
            
            if i == n: # if we evaluated all sticks , then its possbile
                return True
                
            curr_stick = matchsticks[i] # otherwise look at curr stick

            for j in range(4):
                if square[j] + matchsticks[i] <= self.res: # if it CAN fit to a side
                    square[j] += matchsticks[i] 
                    if dfs(i+1, square): # run DFS choosing to add stick on that side and continue 
                        return True
                    square[j] -= matchsticks[i] # backtrack to try another side
            
            return False # otherwise curr stick can't fit in ANY of the sides of curr dfs path so return false
        
        return dfs(0, [0,0,0,0])