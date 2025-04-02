class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[length - 1] != nums[length - 2]:
            return nums[length - 1]
        # Binary search for the single element.
        left = 1
        right = length - 2
        while left <= right:
            mid = left + (right - left) // 2
            # Ensure mid is even to maintain proper pairing.
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
                right = mid - 2
            else:
                left = mid + 2
        return nums[left]
