class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Length of the longest substring without duplicate characters.
        max_length = 0
        # Indices of the last seen ASCII characters.
        char_indices = [-1] * 128
        # Left and right are the bounds of the current substring.
        left = 0
        for right in range(len(s)):
            # Last seen index of the current character.
            index = char_indices[ord(s[right])]
            # Skip the substrings with duplicate characters.
            if index >= left:
                left = index + 1
            char_indices[ord(s[right])] = right
            max_length = max(max_length, right - left + 1)
        return max_length
