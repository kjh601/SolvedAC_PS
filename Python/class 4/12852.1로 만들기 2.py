N = int(input())

dp = [None for _ in range(N+1)]
dp[1] = (0, None)

for i in range(1, N+1):
    for j in [i+1, i*2, i*3]:
        if j > N:
            continue
        if dp[j] and dp[i][0] + 1 >= dp[j][0]:
            continue
        dp[j] = (dp[i][0] + 1, i)

curr = N
result = []
while curr:
    result.append(curr)
    curr = dp[curr][1]

print(str(dp[N][0])+'\n'+' '.join(map(str, result)))
