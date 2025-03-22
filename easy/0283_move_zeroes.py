class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or length == 1:
            return
        zero = -1 # Index of the current first zero element.
        i = 0
        while zero == -1 and i < length:
            if nums[i] == 0:
                zero = i
            i += 1
        if zero == -1:
            # No zero found.
            return nums
        for i in range(zero + 1, length):
            # Find the next non-zero element and swap it with the zero.
            if nums[i] != 0:
                nums[zero] = nums[i]
                nums[i] = 0
                zero += 1
