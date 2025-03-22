class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return length
        k = 0
        for i in range(1, length):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
