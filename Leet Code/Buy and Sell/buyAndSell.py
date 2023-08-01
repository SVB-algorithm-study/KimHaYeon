class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]
        for sell in prices:
            if buy < sell:
                result = max(result, sell - buy)
            else:
                buy = sell
        return result
