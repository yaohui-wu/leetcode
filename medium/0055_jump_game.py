class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy algorithm.
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                # Cannot reach this index.
                return False
            # Update the maximum reachable index.
            max_reach = max(max_reach, i + nums[i])
        return True
