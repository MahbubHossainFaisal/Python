class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 0

        n=len(prices)
        if n<=1:
            return 0
        
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                count+=prices[i]-prices[i-1]
            
        return count