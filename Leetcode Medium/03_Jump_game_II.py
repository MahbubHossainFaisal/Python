# Leetcode : https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        max_distance = 0
        jump_count = 0
        last_jump_idx = 0
        if len(nums)==1:
            return 0

        for i in range(len(nums)):
            max_distance = max(max_distance,i+nums[i])

            if i == last_jump_idx:
                last_jump_idx = max_distance
                jump_count+=1

                if max_distance>=target:
                    return jump_count
        
        return jump_count