class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = [] # Store the result in spiral order.
        # Initialize boundary pointers.
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # Traverse from left to right across the top row.
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            # Traverse from top to bottom along the right column.
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                # Traverse from right to left across the bottom row.
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                # Traverse from bottom to top along the left column.
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result
