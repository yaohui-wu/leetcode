class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1 or nums[0] > nums[1]:
            return 0
        if nums[length - 1] > nums[length - 2]:
            return length - 1
        # Binary search.
        left = 1
        right = length - 2
        while left <= right:
            mid = left + (right - left) // 2
            num = nums[mid]
            # Peak is on the left side.
            if num < nums[mid - 1]:
                right = mid - 1
            # Peak is on the right side.
            elif num < nums[mid + 1]:
                left = mid + 1
            # Peak is found.
            else:
                return mid
        return -1
