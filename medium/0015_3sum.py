class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        length = len(nums)
        for i in range(length):
            target = -nums[i]
            num_to_index = {}
            for j in range(length):
                if i != j:
                    complement = target - nums[j]
                    if complement in num_to_index:
                        solutions.append([nums[i], nums[j], complement])
                    num_to_index[nums[j]] = j
        return solutions
