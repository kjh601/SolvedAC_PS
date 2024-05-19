from sys import stdin
input = stdin.readline

def dfs(r, c):
    count = 0
    x, y = r, c
    visited[x][y] = 1
    route = []
    while True:
        route.append((x,y))
        delta_x, delta_y = deltas[board[x][y]]
        X = x + delta_x
        Y = y + delta_y
        
        if not(0<=X<N and 0<=Y<M):
            for a, b in route:
                exist[a][b] = 1
                count += 1
            return count
        
        if visited[X][Y]:
            for a, b in route:
                exist[a][b] = exist[X][Y]
                count += exist[X][Y]
            return count
        visited[X][Y] = 1
        x, y = X, Y

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
exist = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
deltas = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}
total = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        total += dfs(i,j)

print(total)