import sys
input = sys.stdin.readline

T = int(input())
dp = [0 for _ in range(100)]
dp[0:4] = 1,1,1,2,2
for _ in range(T):
    N = int(input())
    for i in range(5,N):
        dp[i] = dp[i-5]+dp[i-1]
    print(dp[N-1])