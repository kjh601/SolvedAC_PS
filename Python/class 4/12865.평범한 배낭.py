import sys
input = sys.stdin.readline

ans = 0
N, K = map(int, input().split())


dp = [0] * (K+1)
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[K])
