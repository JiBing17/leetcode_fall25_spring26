class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        R = len(board) # num of rows
        C = len(board[0]) # num of cols 

        row = collections.defaultdict(set) # hashset to keep track of what num we have seen in each row
        col = collections.defaultdict(set) # hashset to keep track of what num we have seen in each col
        box = collections.defaultdict(set) # hashset to keep trakc of what num we have seen in each box

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": # skip empty case
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(i//3, j//3)]: # seen already, not valid
                    return False
                
                # add to seen in their appropriate case 
                row[i].add(board[i][j])  
                col[j].add(board[i][j])
                box[(i//3,j//3)].add(board[i][j])

        return True # valid case if we exit the double for loop after checking the entire board 