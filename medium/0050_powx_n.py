class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if x == 1.0 or n == 0:
            return 1.0
        if n < 0:
            # Invert the base and negate the exponent.
            return 1 / x * self.myPow(1 / x, -(n + 1))
        if n % 2 == 0:
            # Square the base and halve the exponent.
            return self.myPow(x * x, n // 2)
        # Reduce n to even and multiply by x.
        return x * self.myPow(x * x,  n // 2)
