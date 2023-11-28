def coin_change(coins,amount):
    max_value = amount + 1  # Use a value greater than the maximum possible number of coins
    memo = [max_value] * (amount + 1)
    memo[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], 1 + memo[i - coin])

    return -1 if memo[amount] == max_value else memo[amount]

                
                
    
    
    
coins = [1,2,5]
amount=11

ans = coin_change(coins,amount)
print(ans)