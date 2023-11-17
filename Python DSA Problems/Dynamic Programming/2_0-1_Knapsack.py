
# Online Python - IDE, Editor, Compiler, Interpreter

def knapsack(capacity,weights,profits,n):
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weights[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],profits[i-1]+ dp[i-1][j-weights[i-1]])
                
    return dp[n][capacity]
                
    

weights = [1,3,4,5]
profits = [1,4,5,7]
capacity = 7
ans = knapsack(capacity,weights,profits,len(weights))
print(ans)