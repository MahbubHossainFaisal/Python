
# Online Python - IDE, Editor, Compiler, Interpreter

def fibonacci(n,memo={}):
    if n in memo:
        return memo[n];
    if n<=2:
        return 1;
        
    else:
        number = fibonacci(n-1,memo) + fibonacci(n-2,memo)
        memo[n] = number
    
    return memo[n]


for i in range(1,11):
    print(fibonacci(i))
