
class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        clone = N
        while N > 0:
            remainder = int(N % 10)
            #print('remainder',remainder)
            N = int(N/10)
            #print('N',N)
            if remainder != 0 and  clone % remainder == 0:
                count+=1
                #print('count',count)
                
                
        return count