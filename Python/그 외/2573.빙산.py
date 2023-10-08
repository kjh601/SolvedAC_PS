import sys
input = sys.stdin.readline


def dfs(i, j, is_visited):
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        for delta_x, delta_y in deltas:
            X = delta_x+x
            Y = delta_y+y
            if is_visited[X][Y]:
                continue
            if board[X][Y] > 0:
                stack.append((X, Y))
                is_visited[X][Y] = 1


def is_seperate():
    is_visited = [[0]*M for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(M):
            if is_visited[i][j]:
                continue
            is_visited[i][j] = 1
            if board[i][j] > 0:
                dfs(i, j, is_visited)
                if count == 1:
                    return 1
                count += 1

    return 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

now = []

for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            now.append((i, j, board[i][j]))

nxt = []
zero_collector = []
count = 0
seperate = 0
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while now:
    x, y, num = now.pop()

    for delta_x, delta_y in deltas:
        X = x+delta_x
        Y = y+delta_y

        if board[X][Y] == 0:
            num -= 1

    if num < 1:
        zero_collector.append((x, y))
    else:
        nxt.append((x, y, num))

    if not now:

        for i, j in zero_collector:
            board[i][j] = 0
        now = nxt
        nxt = []
        count += 1

        if is_seperate():
            seperate = 1
            break

if seperate:
    print(count)
else:
    print(0)
