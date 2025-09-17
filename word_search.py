class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.valid = False # global bool to indicate if we found the word or not
        num_r = len(board) # num of rows in board
        num_c = len(board[0]) # num of cols in board
        seen = set() # set to store visited as (i,j) pair for 2d array traversal
        
        def dfs(i,j,k, visited): # helper dfs for traversing through different ways of forming word from a given i,j position

            if k == len(word): # k index made it to end, found word given this valid path
                self.valid = True # set global var to true in this case
                return

            if (i,j) in seen: # prevent us from exploring positions where we have alredy been to - return
                return
            if i >= num_r or  i < 0: # prevents us from going out of bounds (top to bottom) - return 
                return
            if j < 0 or j >= num_c: # prevents us from going out of bounds (left to right) - return
                return

            if board[i][j] != word[k]: # curr path / curr letter does not match the letter at that position - return
                return

            visited.add((i,j)) # otherwise it does match curr letter at curr position, mark curr position as visited
            k += 1 # advance to check next letter in word for future comparions
            dfs(i-1, j, k, visited) # visit letter at top of curr position
            dfs(i+1, j, k, visited) # visit letter at bottom of curr position
            dfs(i, j+1, k, visited) # visit letter at right of curr positon
            dfs(i, j-1, k, visited) # visit letter at left of curr postion

            visited.remove((i,j)) # at end remove curr pos in visited for next dfs call in the for loop (back tracking)

        for i in range(num_r): # for letter in board 
            for j in range(num_c):
                dfs(i,j,0, seen) # run dfs starting from that letter - see if global bool changes to true or not after the calls
        return self.valid # return the global boolean after exploring entire board 