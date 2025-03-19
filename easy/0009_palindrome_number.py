class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes.
        if x < 0:
            return False
        # Single digit numbers are palindromes.
        if x < 10:
            return True
        reverse = x % 10
        # Positive numbers ending with 0 cannot be palindromes.
        if reverse == 0:
            return False
        # Reverse half of the number and compare it with the other half.
        x //= 10
        while reverse < x:
            reverse *= 10
            reverse += x % 10
            x //= 10
        # Remove the middle digit if the number has an odd number of digits.
        return reverse == x or reverse // 10 == x
