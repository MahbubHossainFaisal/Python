class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sz = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+sz]==needle:
                print(haystack[i:sz])
                return i
        
        return -1
        