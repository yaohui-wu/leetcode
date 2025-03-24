class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Empty list.
        if length == 0:
            return []
        # Entire list is non-negative.
        if nums[0] >= 0:
            return [i * i for i in nums]
        # Entire list is negative.
        if nums[length - 1] < 0:
            nums.reverse()
            return [i * i for i in nums]
        sorted_squares = [0] * length
        left = 0
        right = length - 1
        for i in range(length - 1, -1, -1):
            # Select the larger square.
            if abs(nums[left]) > abs(nums[right]):
                sorted_squares[i] = nums[left] * nums[left]
                left += 1
            else:
                sorted_squares[i] = nums[right] * nums[right]
                right -= 1
        return sorted_squares
