# Leetcode: https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i == '(' or i=='{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if len(stack)>0:
                    ele = stack.pop()
                    if i != mapping[ele]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False