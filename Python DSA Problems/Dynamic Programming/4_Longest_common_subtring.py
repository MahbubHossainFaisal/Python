
def LCS(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    result = 0
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1 
                if dp[i][j] > result:
                    result = dp[i][j]
         
            else:
                dp[i][j] = 0
                
    return result


word1 = 'AOSABBSOAS'
word2 = 'AABQABSWQASS'

ans = LCS(word1,word2)
print(ans)
