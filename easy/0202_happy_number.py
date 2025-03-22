class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set() # Numbers seen.
        while n != 1:
            sum = 0 # Sum of squares of digits.
            while n > 0:
                digit = n % 10
                sum += digit * digit
                n //= 10
            n = sum
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)
        return True
