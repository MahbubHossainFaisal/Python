class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count =0
        s=s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                count+=1

            else:
                break

        return count 