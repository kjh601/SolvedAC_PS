import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
    if arr[i-1] == arr[i]:
        dp[i-1][i] = 1

for k in range(2, N):
    for i in range(N-k):
        j = i + k
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

result = []
for _ in range(M):
    x, y = map(int, input().split())
    result.append(dp[x-1][y-1])

print('\n'.join(map(str,result)))
