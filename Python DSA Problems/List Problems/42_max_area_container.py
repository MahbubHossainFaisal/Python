class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        low = 0
        high = len(height)-1

        while(low<high):

            
            if height[low]<height[high]:
                area = height[low]*(high-low)
                max_area = max(max_area,area)
                low+=1
            else:
                area = height[high]*(high-low)
                max_area = max(max_area,area)
                high-=1
        
        return max_area