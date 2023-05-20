class Solution:
    def armstrongNumber (ob, n):
        # code here 
        clone = n
        sum=0
        while(n>0):
            remainder = int(n%10)
            n=int(n/10)
            sum += remainder**3
            
        if sum == clone:
            return 'Yes'
        else:
            return 'No'