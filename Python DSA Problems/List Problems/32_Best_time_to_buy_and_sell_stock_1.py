class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        n = len(prices)
        if n==0 or n==1:
            return 0
        
        for i in range(1,n):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit,prices[i]-min_price)

        return max_profit