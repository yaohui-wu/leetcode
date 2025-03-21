class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search.
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 # Prevent overflow.
            num = nums[mid]
            if num < target:
                # Search the right half.
                left = mid + 1
            elif num > target:
                # Search the left half.
                right = mid - 1
            else:
                # Found the target.
                return mid
        # Target not found.
        return -1
