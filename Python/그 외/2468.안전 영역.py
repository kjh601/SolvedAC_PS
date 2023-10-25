import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

deltas = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def dfs(loc, is_visited, level):
    stack = [loc]
    is_visited[loc[0]][loc[1]] = 1
    while stack:
        x, y = stack.pop()
        for delta_x, delta_y in deltas:
            X = x+delta_x
            Y = y+delta_y
            if not (0 <= X < N and 0 <= Y < N):
                continue
            if is_visited[X][Y] or board[X][Y] <= level:
                continue
            stack.append((X, Y))
            is_visited[X][Y] = 1


max_count = 0
for level in range(100):
    count = 0
    is_visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= level or is_visited[i][j]:
                continue
            count += 1
            dfs((i, j), is_visited, level)
    if count == 0:
        break
    max_count = max(max_count, count)

print(max_count)
