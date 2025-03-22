class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark the index represented by the current number.
        for i in nums:
            j = abs(i) - 1
            if nums[j] > 0:
                nums[j] = -nums[j]
        disappeared_nums = []
        # The indices of the numbers not marked are the disappeared numbers.
        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared_nums.append(i + 1)
        return disappeared_nums
