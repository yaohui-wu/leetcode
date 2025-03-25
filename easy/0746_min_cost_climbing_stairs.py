class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        second_last = cost[0] # Minimum cost to reach the second last step.
        last = cost[1] # Minimum cost to reach the last step.
        for i in range(2, len(cost)):
            current = cost[i] + min(second_last, last)
            second_last = last
            last = current
        return min(second_last, last)
