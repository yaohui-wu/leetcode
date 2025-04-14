class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        # Flip the matrix vertically.
        for i in range(rows // 2):
            temp = matrix[i]
            matrix[i] = matrix[rows - 1 - i]
            matrix[rows - 1 - i] = temp
        # Transpose the matrix.
        for i in range(rows):
            for j in range(i + 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
