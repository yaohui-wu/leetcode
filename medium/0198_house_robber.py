class Solution:
    def rob(self, nums: List[int]) -> int:
        # Maximum profit including the house before the previous one.
        prev_rob = 0
        # Maximum profit up to the previous house.
        max_rob = 0
        # Compute the maximum profit by choosing to rob or skip the current
        # house.
        for i in nums:
            profit = max(max_rob, prev_rob + i)
            prev_rob = max_rob
            max_rob = profit
        return max_rob
