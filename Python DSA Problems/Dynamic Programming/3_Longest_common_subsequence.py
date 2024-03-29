
# Online Python - IDE, Editor, Compiler, Interpreter


def LCS(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1 
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
                
    return dp[n1][n2]


word1 = 'AOSABBSOAS'
word2 = 'AABQABSWQASS'

ans = LCS(word1,word2)
print(ans)
