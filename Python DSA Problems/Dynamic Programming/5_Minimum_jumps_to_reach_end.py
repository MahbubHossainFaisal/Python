import sys

def minimum_jump(arr):
    n = len(arr)
    max_val = sys.maxsize
    min_jump = [max_val for _ in range(n)]
    min_jump[0] = 0

    for i in range(1, n):
        for j in range(i):
            if arr[j] + j >= i:
                min_jump[i] = min(min_jump[i], min_jump[j] + 1)
                break  # Break once a valid jump is found

    return min_jump[n-1]

arr = [3, 1, 5, 8, 1, 2, 6, 1, 0, 9]
ans = minimum_jump(arr)
print(ans)
