import sys
input = sys.stdin.readline

dp = [[0,0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

last_N = 2
T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(last_N,N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[N][0],dp[N][1])
    last_N = max(last_N,N)
