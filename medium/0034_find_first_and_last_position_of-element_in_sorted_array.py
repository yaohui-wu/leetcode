class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        # Binary search to find the first and last occurrence of the target.
        first = self.find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.find_last(nums, target)
        return [first, last]
    
    def find_first(self, nums, target):
        left = 0
        length = len(nums)
        right = length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # Left is the first occurrence of the target if it exists.
        if left < length and nums[left] == target:
            return left
        return -1
    
    def find_last(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        # Right is the last occurrence of the target if it exists.
        if right >= 0 and nums[right] == target:
            return right
        return -1
