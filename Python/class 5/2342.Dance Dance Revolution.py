from sys import maxsize
INF = maxsize

def cost_move(a, b):
    if a == b:
        return 1
    elif a == 0 or b == 0:
        return 2
    elif abs(a - b) == 2:
        return 4
    else:
        return 3

arr = list(map(int,input().split()))
arr.pop()

dp = [[[INF,INF,INF,INF,INF] for _ in range(5)] for _ in range(len(arr) + 1)]
dp[0][0][0] = 0
for i, k in enumerate(arr,start=1):
    for r in range(5):
        for prev_l in range(5):
            dp[i][k][r] = min(dp[i][k][r], dp[i-1][prev_l][r] + cost_move(prev_l, k))
    for l in range(5):
        for prev_r in range(5):
            dp[i][l][k] = min(dp[i][l][k], dp[i-1][l][prev_r] + cost_move(prev_r, k))
    
min_cost = INF
for i in range(5):
    for j in range(5):
        min_cost = min(min_cost, dp[-1][i][j])
print(min_cost)