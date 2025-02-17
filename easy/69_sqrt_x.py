class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 0
        right = x
        while left < right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square < x:
                left = mid
            elif square > x:
                right = mid
            else:
                return mid
        return left
