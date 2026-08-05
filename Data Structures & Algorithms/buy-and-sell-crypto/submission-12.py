class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        high = prices[0]
        low = prices[0]
        max_profit = 0

        for price in prices:

            if price < low:
                low = price
                high = low

            if price > high:
                high = price
                max_profit = max(max_profit, high - low)
        return max_profit