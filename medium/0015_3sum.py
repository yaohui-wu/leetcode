class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = [] # Unique triplets that sum to zero.
        nums.sort()
        length = len(nums)
        i = 0 # Fix the first element in the triplet.
        while i < length:
            # Skip duplicates for the first element.
            while 0 < i < length - 1 and nums[i] == nums[i - 1]:
                i += 1
            target = -nums[i] # Complement of the first element.
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[j] + nums[k]
                # Need a greater sum.
                if sum < target:
                    j += 1
                # Need a lesser sum.
                elif sum > target:
                    k -= 1
                else:
                    # Found a unique triplet.
                    solution_set.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Skip duplicates for the second element.
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
        return solution_set
