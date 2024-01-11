# Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[j-2]:
                nums[j]=nums[i]
                j+=1

        return j
            
