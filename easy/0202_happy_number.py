class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        num = n
        while n not in nums:
            sum = 0
            while num > 0:
                digit = num % 10
                sum += digit * digit
                num //= 10
            if sum == 1:
                return True
            if sum in nums:
                return False
            nums.add(sum)
            num = sum
        return False
