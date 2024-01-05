#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_num=nums[0]
        count = 1
        k=1
        
        if len(nums) == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == current_num:
                count+=1
                if count<=2:
                    nums[k] = nums[i]
                    k+=1
            else:
                current_num = nums[i]
                nums[k]=nums[i]
                k+=1
                count=1

        return k
        
       