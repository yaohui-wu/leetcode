class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        index = length
        char_to_entry = {} # char -> [count, index].
        for i in range(length):
            if s[i] in char_to_entry:
                entry = char_to_entry[s[i]]
                entry[0] += 1
                entry[1] = i
            else:
                char_to_entry[s[i]] = [1, i]
        for entry in char_to_entry.values():
            if entry[0] == 1:
                index = min(index, entry[1])
        if index == length:
            return -1
        return index
