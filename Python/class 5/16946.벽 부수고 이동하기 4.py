from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write

def bfs(start):
    queue = deque()
    stack = deque()
    visited_wall = set()
    queue.append(start)
    count = 1
    deltas = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y = queue.pop()
        for delta_x, delta_y in deltas:
            X = x+delta_x
            Y = y+delta_y
            if not (0<=X<N and 0<=Y<M) or visited[X][Y]:
                continue
            if board[X][Y] == 0:
                queue.appendleft((X,Y))
                visited[X][Y] = True
                count += 1
            elif (X,Y) not in visited_wall :
                stack.append((X,Y))
                visited_wall.add((X,Y))
    while stack:
        x, y = stack.pop()
        board[x][y] += count

N,M = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            bfs((i,j))
for i in range(N):
    for j in range(M):
        board[i][j] %= 10

output('\n'.join(''.join(map(str, line)) for line in board)+'\n')
