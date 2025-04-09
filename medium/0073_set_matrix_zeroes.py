class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # Flags to track if the first row and the first column should be
        # zeroed.
        is_first_row_zero = False
        is_first_col_zero = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = True
                    if j == 0:
                        is_first_col_zero = True
                    # Mark the first cell of the row and the first cell of the
                    # column as 0.
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # Set the cells to 0 based on the first row and first column.
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if is_first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if is_first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
