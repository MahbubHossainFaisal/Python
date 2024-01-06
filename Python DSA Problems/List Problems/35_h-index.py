import math
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(len(citations)):
            if n - i <= citations[i]:
                return n - i
        return 0