# Leetcode link: https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I',
        }
        ans=''
        while num>0:
            if num==0:
                return ans
            
            for key,val in table.items():
                if key<=num:
                    num-=key
                    ans+=val
                    break
        
        return ans