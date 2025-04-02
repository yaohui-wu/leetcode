class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        m = len(matrix) # Number of rows.
        n = len(matrix[0]) # Number of columns.
        # Bounds for binary search.
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # Convert mid to row and column indices.
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid - 1
            else:
                return True
        return False
