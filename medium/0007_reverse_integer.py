class Solution:
    def reverse(self, x: int) -> int:
        limit = 2 ** 31 - 1 # Maximum signed 32-bit integer.
        signed = False
        if x < 0:
            signed = True
        x = abs(x)
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        if reverse > limit:
            return 0
        if signed:
            return -reverse
        return reverse
