class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        second_last = cost[0]
        last = cost[1]
        for i in range(2, len(cost)):
            min_cost = min(second_last, last) + cost[i]
            second_last = last
            last = min_cost
        return min_cost