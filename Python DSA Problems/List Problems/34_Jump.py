# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_idx = len(nums)-1
        flag=False
        if len(nums)==1:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] != 0:
                if nums[i] >= target_idx-i:
                    target_idx = i
                    flag = True
                else:
                    flag = False

        return flag