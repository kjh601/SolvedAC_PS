N = int(input())
dp = [1,3]
for i in range(2,N):
    dp.append((dp[i-1]+2*dp[i-2]))
print(dp[N-1]%10007)