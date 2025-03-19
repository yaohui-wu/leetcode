class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases.
        if n == 1 or n == 2:
            return n
        # Dynamic programming.
        prev_two = 1 # Ways to reach previous two steps.
        prev = 2 # Ways to reach previous step.
        total = 3 # Ways to reach current step.
        for _ in range (3, n):
            # Move one step and update the values.
            prev_two = prev
            prev = total
            total = prev + prev_two
        return total
