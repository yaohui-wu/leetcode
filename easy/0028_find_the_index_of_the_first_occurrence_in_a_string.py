class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        # Needle is longer than haystack.
        if needle_len > haystack_len:
            return -1
        # Empty needle.
        elif needle_len == 0:
            return 0
        # Search for the needle in the haystack.
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1
