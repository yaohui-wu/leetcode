class Solution:
    def romanToInt(self, s: str) -> int:
        # Map the roman numeral to integer.
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                        "M": 1_000}
        length = len(s)
        num = roman_to_int[s[length - 1]] # Last numeral.
        for i in range(length - 1):
            current = roman_to_int[s[i]]
            next = roman_to_int[s[i + 1]]
            # Subtract if smaller numeral precedes larger one, else add.
            if current < next:
                num -= current
            else:
                num += current
        return num
