class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        answer = 0
        for sell in prices:
            if buy < sell:
                answer += sell - buy
                buy = sell
            else:
                buy = sell
        return answer
            
