from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = 0
        for word in word_set:
            if len(word) > max_len:
                max_len = len(word)
        # dp[i] means s[:i] can be segmented into words in wordDict.
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented.
        for i in range(1, len(s)+ 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]
