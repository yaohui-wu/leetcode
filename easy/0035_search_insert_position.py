class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        # Target is less than the least element.
        if nums[left] > target:
            return 0
        right = len(nums) - 1
        # Target is greater than the greatest element.
        if nums[right] < target:
            return right + 1
        # Binary search.
        while left <= right:
            mid = left + (right - left) // 2 # Avoid overflow.
            num = nums[mid]
            if num < target:
                # Search right half.
                left = mid + 1
            elif num > target:
                # Search left half.
                right = mid - 1
            else:
                # Found the target.
                return mid
        # Return the index after the greatest element less than the target.
        return right + 1
