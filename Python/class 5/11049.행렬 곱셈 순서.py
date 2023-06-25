import sys
input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(i, n):
        x = j - i
        dp[x][j] = 2**32
        for k in range(x, j):
            dp[x][j] = min(dp[x][j], dp[x][k] + dp[k+1][j] + arr[x][0]*arr[k][1]*arr[j][1])

print(dp[0][n-1])
