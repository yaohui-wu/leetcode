class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i
        return -1
