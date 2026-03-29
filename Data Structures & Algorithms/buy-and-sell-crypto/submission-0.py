class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        for prev_day in range(len(prices)):
            for today in range(prev_day+1, len(prices)):
                if prices[today] > prices[prev_day]:
                    profit = prices[today] - prices[prev_day]
                    max_profit = max(profit, max_profit)
                else: 
                    continue

        return max_profit