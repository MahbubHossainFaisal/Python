# Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_prof+=prices[i]-prices[i-1]
            
        return max_prof
        