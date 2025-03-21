class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or length == 1:
            return
        zero = -1
        found = False
        i = 0
        while not found and i < length:
            if nums[i] == 0:
                found = True
                zero = i
            i += 1
        if not found:
            return nums
        next_zero = -1
