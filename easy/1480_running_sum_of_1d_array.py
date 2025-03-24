class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return []
        sums = [nums[0]]
        for i in range(1, length):
            sums.append(sums[i - 1] + nums[i])
        return sums
