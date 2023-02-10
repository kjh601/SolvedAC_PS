import sys
input = sys.stdin.readline

T = int(input())
prev_N = 4
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    N = int(input())
    if N>3:
        for i in range(prev_N,N+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        prev_N = N+1
    print(dp[N])