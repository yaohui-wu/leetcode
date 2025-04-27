class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic programming.
        # changes[i] = minimum number of coins needed to make amount i.
        # Initialize changes array with amount + 1 (infinity).
        changes = [amount + 1] * (amount + 1)
        changes[0] = 0
        # Iterate through all amounts and update the minimum coins required.
        for i in range(1, len(changes)):
            for coin in coins:
                if i >= coin:
                    changes[i] = min(changes[i], changes[i - coin] + 1)
        if changes[amount] == amount + 1:
            # No solution found.
            return -1
        return changes[amount]
