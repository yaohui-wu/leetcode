class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0 # Buy.
        right = 1 # Sell.
        length = len(prices)
        # Compute the profits of all possible trades with the lowest buy price
        # and highest sell price.
        while right < length:
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            elif profit < 0:
                # New lowest price to buy.
                left = right
            right += 1
        return max_profit
