class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit * digit
                n //= 10
            if sum == 1:
                return True
            if sum in nums:
                return False
            nums.add(sum)
            n = sum
        return True
