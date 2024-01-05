# https://leetcode.com/problems/remove-element/submissions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        temp=0
    
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        

        return k