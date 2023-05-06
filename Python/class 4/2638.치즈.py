from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_exposed_cheese():
    queue = deque([(0, 0)])
    exposed_cheese = defaultdict(int)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        x, y = queue.pop()
        for delta_x, delta_y in deltas:
            X = x+delta_x
            Y = y+delta_y
            if not (0 <= X < N and 0 <= Y < M) or visited[X][Y]:
                continue
            if board[X][Y] == 1:
                exposed_cheese[(X, Y)] += 1
                continue
            queue.appendleft((X, Y))
            visited[X][Y] = 1
    return [loc for loc, cnt in exposed_cheese.items() if cnt > 1]


count = 0
while True:
    exposed_cheese = get_exposed_cheese()
    if not exposed_cheese:
        break
    for x, y in exposed_cheese:
        board[x][y] = 0
    count += 1
print(count)
