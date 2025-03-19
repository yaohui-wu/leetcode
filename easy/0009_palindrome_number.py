class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes.
        if x < 0:
            return False
        # Single digit numbers are palindromes.
        if x < 10:
            return True
        # Reverse the number and check if it is the same as the original.
        reverse = x % 10
        num = x // 10
        while num > 0:
            reverse *= 10
            reverse += num % 10
            num //= 10
        return reverse == x
