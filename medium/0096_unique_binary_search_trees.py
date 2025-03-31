class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        num_trees = 1 # Number of unique BSTs.
        # Equivalent to the Catalan number C(n) for n >= 0.
        # C(0) = 1, C(n) = sum(C(i - 1) * C(n - i)) for i from 1 to n.
        # C(n) = (2n)! / ((n + 1)! * n!)
        factorial = 1
        for i in range(2, n * 2 + 1):
            factorial *= i
            if i == n or i == n + 1:
                num_trees *= factorial
        num_trees = factorial // num_trees
        return num_trees
