class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # Eliminate duplicates.
        length = 0 # Length of the longest consecutive elements sequence.
        for x in nums_set:
            # Check if x is the start of a sequence.
            if x - 1 not in nums_set:
                y = x + 1
                # Count consecutive numbers starting from x.
                while y in nums_set:
                    y += 1
                length = max(length, y - x)
        return length
