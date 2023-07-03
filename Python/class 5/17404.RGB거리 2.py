import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]

dp = [[INF,INF,INF] for _ in range(N+1)]

result = INF

arr = [(0,1,2),(1,0,2),(2,0,1)]

for x,y,z in arr:
    dp[0][x] = cost[0][x]
    for j in range(1,N):
        for X,Y,Z in arr:
            dp[j][X] = min(dp[j-1][Y], dp[j-1][Z])+cost[j][X]
    result = min(result, dp[N-1][y], dp[N-1][z])
    dp[0][x] = INF

print(result)