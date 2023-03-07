from collections import deque
import sys
input = sys.stdin.readline


def is_all_one_color(row, col, length, color):
    for i in range(row, row+length):
        for j in range(col, col+length):
            if board[i][j] != color:
                return 0
    return 1


def bfs(start):
    queue = deque([start])

    while queue:
        x, y, length = queue.popleft()
        if is_all_one_color(x, y, length, board[x][y]):
            count[board[x][y]] += 1
        else:
            deltas = [(0, 0),
                      (length//2, 0),
                      (0, length//2),
                      (length//2, length//2)]
            for delta_x, delta_y in deltas:
                X = x+delta_x
                Y = y+delta_y
                queue.append((X, Y, length//2))


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
count = [0, 0]

bfs((0, 0, N))

for num in count:
    print(num)
