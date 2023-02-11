N = int(input())
dp = [0 for _ in range(N)]
dp[:2] = 1,2,3
for i in range(3,N):
    dp[i] = (dp[i-1]+dp[i-2])%10007
print(dp[N-1])