class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return []
        if nums[0] >= 0:
            return [i * i for i in nums]
        if nums[length - 1] < 0:
            nums.reverse()
            return [i * i for i in nums]
        right = 1
        while right < length and nums[right] < 0:
            right += 1
        sorted = []
        left = right - 1
        while left >= 0 and right < length:
            if abs(nums[left]) < nums[right]:
                sorted.append(nums[left])
                left -= 1
            else:
                sorted.append(nums[right])
                right += 1
        for i in range(left, -1, -1):
            sorted.append(nums[i])
        for i in range(right, length):
            sorted.append(nums[i])
        return [i * i for i in sorted]
