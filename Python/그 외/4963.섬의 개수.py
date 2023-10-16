import sys
input = sys.stdin.readline
write = sys.stdout.write

deltas = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]


def dfs(x, y, W, H, board, is_visited):

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for delta_x, delta_y in deltas:
            X = x+delta_x
            Y = y+delta_y
            if not (0 <= X < H and 0 <= Y < W):
                continue
            if is_visited[X][Y] or board[X][Y] == 0:
                continue
            stack.append((X, Y))
            is_visited[X][Y] = 1


def solve(W, H):
    count = 0
    board = [list(map(int, input().split())) for _ in range(H)]

    is_visited = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0 or is_visited[i][j]:
                continue
            dfs(i, j, W, H, board, is_visited)
            count += 1
    return count


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    write(str(solve(w, h))+'\n')
