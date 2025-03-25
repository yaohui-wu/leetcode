class Solution:
    def fib(self, n: int) -> int:
        # # Base cases: F(0) = 0 and F(1) = 1.
        if n == 0 or n == 1:
            return n
        second_last = 0 # F(n-2).
        last = 1 # F(n-1).
        for _ in range(2, n + 1):
            current = last + second_last # F(n) = F(n-1) + F(n-2).
            second_last = last # Move F(n-2) forward.
            last = current # Move F(n-1) forward.
        # Return F(n).
        return last
