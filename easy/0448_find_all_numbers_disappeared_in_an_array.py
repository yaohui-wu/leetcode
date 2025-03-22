class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        disappeared_nums = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                disappeared_nums.append(i)
        return disappeared_nums
