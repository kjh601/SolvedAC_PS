import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dists = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dists[i][j] = -1


def bfs(start):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    curr = [start]
    nxt = []
    visited = {start}
    dist = 0
    while curr:
        x, y = curr.pop()
        dists[x][y] = dist
        for delta_x, delta_y in deltas:
            X = x + delta_x
            Y = y + delta_y
            if 0 <= X < n and 0 <= Y < m and (X, Y) not in visited and board[X][Y] == 1:
                nxt.append((X, Y))
                visited.add((X, Y))
        if not curr:
            curr = nxt
            nxt = []
            dist += 1


for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start = (i, j)
            break

bfs(start)
for line in dists:
    print(' '.join(map(str, line))+'\n')
