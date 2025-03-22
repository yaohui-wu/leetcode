class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = 0 # Size of the current window of zeroes.
        for i in range(len(nums)):
            if nums[i] == 0:
                size += 1 # Expand the window.
            elif size > 0:
                # Swap the current non-zero element with the first zero in the
                # window.
                nums[i - size] = nums[i]
                nums[i] = 0
