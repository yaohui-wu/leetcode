class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        length = len(nums)
        if length < 3 or nums[0] > 0:
            return solution
        num_to_index = {}
        for i in range(length):
            num_to_index[nums[i]] = i
        i = 0
        while i < length - 2 and nums[i] <= 0:
            j = i + 1
            while j < length - 1:
                target = -(nums[i] + nums[j])
                if target in num_to_index and num_to_index[target] > j:
                    solution.append([target, nums[i], nums[j]])
                j = num_to_index[nums[j]] + 1
            i = num_to_index[nums[i]] + 1
        return solution
