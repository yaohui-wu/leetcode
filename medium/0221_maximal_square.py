class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Dynamic programming.
        rows = len(matrix)
        cols = len(matrix[0])
        # sizes[i] = length of the largest square with bottom right corner at
        # (i, j).
        sizes = [[0] * cols for _ in range(rows)]
        size = 0 # Maximal square size.
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        # Base case: first row or column.
                        sizes[i][j] = 1
                    else:
                        # Update the size based on neighboring squares.
                        top_left = sizes[i - 1][j - 1]
                        top = sizes[i - 1][j]
                        left = sizes[i][j - 1]
                        sizes[i][j] = min(top_left, top, left) + 1
                if sizes[i][j] > size:
                    size = sizes[i][j]
        # Return the area of the largest square.
        return size * size
