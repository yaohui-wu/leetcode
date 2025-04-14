class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Maps to track the last seen index of characters in s and t.
        s_map = [0] * 256
        t_map = [0] * 256
        for i in range(len(s)):
            if s_map[ord(s[i])] != t_map[ord(t[i])]:
                return False
            # Update last seen index for both characters.
            s_map[ord(s[i])] = i + 1
            t_map[ord(t[i])] = i + 1
        return True
