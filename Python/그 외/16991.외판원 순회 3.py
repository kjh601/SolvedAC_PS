import sys
input = sys.stdin.readline

N = int(input())

INF = int(1e9)
dp = [[-1]*(1 << N) for _ in range(N)]

node = [tuple(map(int,input().split())) for _ in range(N)]

def dfs(now, visited):
    if visited == (1 << N)-1:
        if not graph[now][0]:
            return INF
        return graph[now][0]

    if dp[now][visited] != -1:
        return dp[now][visited]
    dp[now][visited] = INF

    for nxt in range(1, N):
        if not graph[now][nxt]:
            continue
        if visited & (1 << nxt):
            continue

        dp[now][visited] = min(dp[now][visited],
                               dfs(nxt, visited | (1 << nxt)) + graph[now][nxt])
    return dp[now][visited]

def cal_dist(node1, node2):
    return((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)**0.5

graph = [[cal_dist(node[i], node[j]) for j in range(N)] for i in range(N)]
print(dfs(0, 1))
