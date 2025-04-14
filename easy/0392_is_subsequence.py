class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        if s_length > t_length:
            return False
        if s_length == 0:
            return True
        i = 0 # Index of current character in s.
        # Match characters in s with characters in t maintaining the order.
        for j in range(t_length):
            if s[i] == t[j]:
                i += 1
                if i == s_length:
                    return True
        return False
