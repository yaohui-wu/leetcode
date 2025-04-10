class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # Normalize k to be within the array length.
        k %= length
        # Reverse the entire array.
        self.reverse(nums, 0, length - 1)
        # Reverse the first k elements.
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining elements.
        self.reverse(nums, k, length - 1)
    
    def reverse(self, nums, left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
