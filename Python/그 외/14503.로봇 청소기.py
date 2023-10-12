import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1
    is_clean = True
    for dir in range(d+3, -1, -1):
        dir %= 4
        delta_r, delta_c = deltas[dir]
        row = r+delta_r
        col = c+delta_c
        if not (0 <= row < N and 0 <= col < M):
            continue
        if board[row][col] == 0:
            r, c, d = row, col, dir
            is_clean = False
            break
    if is_clean:
        delta_r, delta_c = deltas[(d+2) % 4]
        r += delta_r
        c += delta_c

    if not (0 <= r < N and 0 <= c < M) or board[r][c] == 1:
        break

print(count)
