class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
            if frequency[i] > majority:
                return i
        return -1
