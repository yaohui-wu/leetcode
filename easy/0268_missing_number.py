class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Formula for the sum of first n natural numbers by Gauss.
        sum = n * (n + 1) // 2
        for i in nums:
            sum -= i
        # The missing number is the remaining sum.
        return sum
