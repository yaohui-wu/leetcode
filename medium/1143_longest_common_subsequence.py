class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Dynamic programming.
        if len(text1) < len(text2):
            # Shorter string is the column.
            text1, text2 = text2, text1
        # Previous row of the DP table.
        prev = [0] * (len(text2) + 1) # Handle empty string comparisons.
        for i in range(1, len(text1) + 1):
            curr = [0] * (len(text2) + 1) # Current row.
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match so extend the LCS.
                    curr[j] = 1 + prev[j - 1]
                else:
                    # Take the maximum LCS possible by skipping the current
                    # character from either string.
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        # The last value is the length of the LCS.
        return prev[-1]
