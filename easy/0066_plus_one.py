class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1 # Start from the last digit.
        digits[i] += 1 # Add 1 to the last digit.
        # Carry the 1 to the previous digit if the digit is 10.
        while digits[i] == 10:
            digits[i] = 0
            # If the first digit is 10, insert 1 to the front.
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
            i -= 1
        return digits
