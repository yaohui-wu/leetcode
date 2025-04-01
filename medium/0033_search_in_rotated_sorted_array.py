class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search.
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            # Negative infinity case.
            if target < nums[0] < num:
                left = mid + 1
            # Positive infinity case.
            elif num < nums[0] <= target:
                right = mid
            elif num < target:
                left = mid + 1
            elif num > target:
                right = mid
            else:
                return mid
        return -1
