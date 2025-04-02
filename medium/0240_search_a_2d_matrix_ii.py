class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # Number of rows.
        n = len(matrix[0]) # Number of columns.
        # Start from the top-right corner.
        row = 0
        col = n - 1
        while row < m and col >= 0:
            num = matrix[row][col]
            # Move down.
            if num < target:
                row += 1
            # Move left.
            elif num > target:
                col -= 1
            else:
                return True
        return False
