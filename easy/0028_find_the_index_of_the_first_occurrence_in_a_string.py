class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        diff = haystack_len - needle_len
        if diff < 0:
            return -1
        left = 0
        right = needle_len - 1
        while right < haystack_len:
            i = needle_len - 1
            j = right
            while i >= 0 and needle[i] == haystack[j]:
                i -= 1
                j -= 1
            if i == -1:
                return left
            left += 1
            right += 1
        return -1
