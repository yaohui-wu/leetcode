class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or length == 1:
            return
        zeroes = 0 # Size of the current window of zeroes.
        for i in range(length):
            if nums[i] == 0:
                zeroes += 1 # Expand the window.
            elif zeroes > 0:
                # Swap the current non-zero element with the first zero in the
                # window.
                nums[i - zeroes] = nums[i]
                nums[i] = 0
