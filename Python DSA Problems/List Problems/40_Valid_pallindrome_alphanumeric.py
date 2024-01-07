class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s)-1
        s = s.lower()
        while(first<=last):
            if not s[first].isalnum():
                first+=1
            elif not s[last].isalnum():
                last-=1
            elif s[first]!=s[last]:
                return False
            else:
                first+=1
                last-=1

        return True
            
        