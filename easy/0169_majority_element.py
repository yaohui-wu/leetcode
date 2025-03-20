class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2 # Majority threshold.
        frequencies = {} # Frequency of each element.
        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1
            if frequencies[i] > majority:
                return i
        return -1
