class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0] * cols for _ in range(rows)]
        # First pass: top-left to bottom-right.
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    # Compute distance from top and left neighbors.
                    top = dp[i - 1][j] if i > 0 else float("inf")
                    left = dp[i][j - 1] if j > 0 else float("inf")
                    dp[i][j] = min(top, left) + 1
        # Second pass: bottom-right to top-left.
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j] != 0:
                    # Compute distance from bottom and right neighbors.
                    bottom = dp[i + 1][j] if i < rows - 1 else float("inf")
                    right = dp[i][j + 1] if j < cols - 1 else float("inf")
                    dp[i][j] = min(dp[i][j], bottom + 1, right + 1)
        return dp
