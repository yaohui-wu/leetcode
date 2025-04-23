class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # Number of rows.
        cols = len(matrix[0]) # Number of columns.
        # Start from the top-right corner.
        row1 = 0
        col1 = cols - 1
        # Start from the bottom-left corner.
        row2 = rows - 1
        col2 = 0
        while self.is_valid(row1, col1, row2, col2, rows, cols):
            num1 = matrix[row1][col1]
            num2 = matrix[row2][col2]
            if num1 < target:
                row1 += 1
            elif num1 > target:
                col1 -= 1
            else:
                return True
            if num2 < target:
                col2 += 1
            elif num2 > target:
                row2 -= 1
            else:
                return True
        return False
    
    def is_valid(self, row1, col1, row2, col2, rows, cols):
        return row1 < rows and 0 <= col1 and 0 <= row2 and col2 < cols
