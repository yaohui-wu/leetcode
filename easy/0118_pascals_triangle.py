class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(i + 1):
                if j != 0 and j != i:
                    num = pascals[i - 1][j - 1] + pascals[i - 1][j]
                    pascals[i][j] = num
        return pascals
