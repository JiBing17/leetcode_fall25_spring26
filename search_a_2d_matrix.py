class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        rows = len(matrix) # get num of rows in matrix
        cols = len(matrix[0]) # get num of cols in matrix

        l,r = 0, rows - 1 # define left and right pointer for searching based on first element in each row
        
        new_r = -1 # var used to find the correct row target is in
        while l <= r: # binary search
            mid = (l+r) // 2
            val_start = matrix[mid][0] # first element in selected row 
            val_end = matrix[mid][-1] # last element in selected row 
            if val_start <= target and target <= val_end: # if target is within bound
                new_r = mid # that's the correct row to binary search on
                break
            elif target < val_start: # adjust right pointer to find row that contains a smaller first element 
                r = mid - 1
            else: 
                l = mid + 1 # same for left if we want the next row to conain a bigger first element

        l = 0 
        r = cols-1 
        while l <= r: # normal binary search after figuring out which row to search for target in matrix 
            mid = (r + l) // 2
            val = matrix[new_r][mid]
            if val == target:
                return True
            elif val > target: 
                r -= 1
            else:
                l += 1
        return False