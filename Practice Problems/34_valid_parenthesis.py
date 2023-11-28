class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i not in mapping:
                stack.append(i)
            else:
                top_ele = stack.pop() if stack else '#'
                if mapping[i] != top_ele:
                    return False
        
        return not stack
        