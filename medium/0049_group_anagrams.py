class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map the sorted string to its anagrams.
        sorted_to_words = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in sorted_to_words:
                sorted_to_words[sorted_s].append(s)
            else:
                sorted_to_words[sorted_s] = [s]
        return list(sorted_to_words.values())
