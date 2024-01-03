class Solution:
    def reverse(self,s,s2):
        if len(s)<=1:
            return
        while (len(s) != 1):
            ele = s.pop()
            s2.append(ele)
        
        top_ele = s.pop()

        while (len(s2)!=0):
            ele = s2.pop()
            s.append(ele)

        self.reverse(s,s2)
        s.append(top_ele) 


    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s2=[]
        self.reverse(s,s2)
