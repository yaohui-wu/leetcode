class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.backtrack(nums, answer, 0)
        return answer
    
    def backtrack(self, nums, answer, position):
        if position == len(nums):
            # All positions are fixed so we have a valid permutation.
            answer.append(nums[:])
            return
        for i in range(position, len(nums)):
            # Fix a number at the current position.
            nums[position], nums[i] = nums[i], nums[position]
            # Move to the next position.
            self.backtrack(nums, answer, position + 1)
            # Backtrack to the previous state.
            nums[position], nums[i] = nums[i], nums[position]
