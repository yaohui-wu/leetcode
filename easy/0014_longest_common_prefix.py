class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = "" # Longest common prefix.
        shortest_s = min(strs, key=len)
        i = 0
        length = len(shortest_s)
        while i < length:
            c = shortest_s[i]
            for s in strs:
                if s[i] != c:
                    return lcp
            lcp += c
            i += 1
        return lcp
