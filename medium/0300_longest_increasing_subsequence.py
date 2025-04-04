class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic Programming.
        length = len(nums)
        # lengths[i] = length of the longest increasing subsequence that ends
        # with nums[i].
        lengths = [1] * length
        for i in range(1, length):
            for j in range(i):
                # Extend the subsequence and update the longest length.
                if nums[i] > nums[j]:
                    lengths[i] = max(lengths[i], lengths[j] + 1)
        max_length = -1 # Length of the longest increasing subsequence.
        for i in lengths:
            if i > max_length:
                max_length = i
        return max_length
