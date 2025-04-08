class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    # Found an unvisited island.
                    islands += 1
                    # Use DFS to mark all parts of the island as visited.
                    self.dfs(grid, rows, cols, i, j)
        return islands
    
    def dfs(self, grid, rows, cols, i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            # Out of bounds or at water.
            return
        grid[i][j] = "0" # Mark as visited.
        # Recursively explore all four directions: up, down, left, and right.
        self.dfs(grid, rows, cols, i - 1, j)
        self.dfs(grid, rows, cols, i + 1, j)
        self.dfs(grid, rows, cols, i, j - 1)
        self.dfs(grid, rows, cols, i, j + 1)
