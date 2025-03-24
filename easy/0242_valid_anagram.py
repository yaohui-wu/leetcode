class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Frequency of each letter (26 letters in the alphabet).
        letters = [0] * 26
        first = ord("a") # ASCII value of 'a'.
        # Count the frequency of each letter in s.
        for c in s:
            letters[ord(c) - first] += 1
        # Subtract the frequency of each letter in t.
        for c in t:
            letters[ord(c) - first] -= 1
        # If all the frequencies are 0, then s and t are anagrams.
        for i in letters:
            if i != 0:
                return False
        return True
