class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()
        for i in nums:
            if i in distinct_nums:
                return True
            distinct_nums.add(i)
        return False
