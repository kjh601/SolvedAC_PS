N = int(input())
dp = [[[0]*1024 for _ in range(10)]for _ in range(N+1)]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            if 1 <= j:
                dp[i][j][k | (1 << j)] += dp[i-1][j-1][k]
            if j < 9:
                dp[i][j][k | (1 << j)] += dp[i-1][j+1][k]
            dp[i][j][k | (1 << j)] %= 1000000000

total = 0
for i in range(1, 10):
    total += dp[N][i][1023]
    total %= 1000000000

print(total)
