class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or length == 1:
            return
        zero = -1
        i = 0
        while zero == -1 and i < length:
            if nums[i] == 0:
                zero = i
            i += 1
        if zero == -1:
            return nums
        for i in range(zero + 1, length):
            num = nums[i]
            if num != 0:
                nums[zero] = num
                nums[i] = 0
                zero += 1
