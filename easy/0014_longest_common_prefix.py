class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Empty list, return empty string.
        if len(strs) == 0:
            return ""
        # Longest common prefix (LCP) cannot be longer than the shortest
        # string.
        shortest_s = min(strs, key=len)
        for i in range(len(shortest_s)):
            c = shortest_s[i] # Character to compare.
            # Check if the character is the same in all strings.
            for s in strs:
                if s[i] != c:
                    # Mismatch found, return the LCP found so far.
                    return shortest_s[:i]
        return shortest_s
