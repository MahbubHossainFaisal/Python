class Solution:
    def reversedBits(self, X):
        # code here 
        bin_num = format(X,'032b')
        #print(len(str(bin_num)))
        reverse_bin_str = str(bin_num)[::-1]
        decimal_value = int(reverse_bin_str,2)
        return decimal_value
        
        